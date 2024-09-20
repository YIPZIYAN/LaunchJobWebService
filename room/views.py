from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response

from room.models import Room
from room.serializer import RoomSerializer


@api_view(['GET'])
def index(request):
    return Response(RoomSerializer(Room.objects.all(), many=True).data)
