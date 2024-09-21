from rest_framework import serializers

from skilltest.models import SkillTest, Question, Option


class OptionSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    text = serializers.CharField(required=True, max_length=1000)
    is_correct = serializers.BooleanField(required=True)

    class Meta:
        model = Option
        fields = ('id', 'text', 'is_correct')

    def create(self, validated_data):
        return Option.objects.create(**validated_data)


class QuestionSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    text = serializers.CharField(required=True, max_length=1000)
    points = serializers.IntegerField(required=True)
    options = OptionSerializer(many=True)

    class Meta:
        model = Question
        fields = ('id', 'text', 'points', 'options')

    def create(self, validated_data):
        options_data = validated_data.pop('options')
        question = Question.objects.create(**validated_data)
        for option_data in options_data:
            Option.objects.create(question=question, **option_data)
        return question


class SkillTestSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(required=True, max_length=100)
    description = serializers.CharField(required=True, max_length=1000)
    questions = QuestionSerializer(many=True)  # Nested serializer for questions

    class Meta:
        model = SkillTest
        fields = ('id', 'name', 'description', 'questions')

    def create(self, validated_data):
        questions_data = validated_data.pop('questions')
        skill_test = SkillTest.objects.create(**validated_data)
        for question_data in questions_data:
            options_data = question_data.pop('options')
            question = Question.objects.create(skill_test=skill_test, **question_data)
            for option_data in options_data:
                Option.objects.create(question=question, **option_data)
        return skill_test





