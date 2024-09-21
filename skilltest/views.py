from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from skilltest.models import SkillTest, Question, Option
from skilltest.serializer import SkillTestSerializer


@api_view(['GET'])
def index(request):
    return Response(SkillTestSerializer(SkillTest.objects.all(), many=True).data)


@api_view(['POST'])
def store(request):
    serializer = SkillTestSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def submit_test(request):
    skill_test_id = request.data.get('skill_test_id')
    submitted_answers = request.data.get('submitted_answers')

    try:
        skill_test = SkillTest.objects.get(id=skill_test_id)
    except SkillTest.DoesNotExist:
        return Response({"error": "Skill test not found."}, status=404)

    total_correct_points = 0
    total_possible_points = 0

    # Loop through the submitted answers and calculate the score based on points
    for answer in submitted_answers:
        question_id = answer['question_id']
        selected_option_id = answer['selected_option_id']

        # Ensure the question belongs to the skill test
        try:
            question = Question.objects.get(id=question_id, skill_test=skill_test)
        except Question.DoesNotExist:
            return Response({"error": f"Question {question_id} not found in the skill test."}, status=404)

        # Get the selected option
        try:
            selected_option = Option.objects.get(id=selected_option_id, question=question)
        except Option.DoesNotExist:
            return Response({"error": f"Option {selected_option_id} not found for question {question_id}."}, status=404)

        # Add the points for this question to the total possible points
        total_possible_points += question.points

        # Check if the selected option is correct
        if selected_option.is_correct:
            total_correct_points += question.points

    # Calculate the percentage score based on the total points
    if total_possible_points > 0:
        percentage = (total_correct_points / total_possible_points) * 100
    else:
        percentage = 0

    # Return the score results
    score = {
        'total_correct_points': total_correct_points,
        'total_possible_points': total_possible_points,
        'percentage': percentage
    }

    return Response(score)

