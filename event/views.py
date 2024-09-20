from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response

from event.models import Event
from event.serializer import EventSerializer


@api_view(['GET'])
def index(request):
    return Response(EventSerializer(Event.objects.all(), many=True).data)
