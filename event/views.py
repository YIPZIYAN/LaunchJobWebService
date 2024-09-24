from datetime import datetime

from django.conf import settings
import pytz
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from event.models import Event, EventAttendee, Attendee
from event.serializer import EventSerializer, AttendeeSerializer, EventAttendeeSerializer


@api_view(['GET'])
def index(request):
    local_tz = pytz.timezone(settings.TIME_ZONE)
    today = datetime.now(local_tz).date()
    events = Event.objects.filter(start_date__gte=today)
    return Response(EventSerializer(events, many=True).data)


@api_view(['POST'])
def store(request):
    serializer = EventSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def attendee(request):
    serializer = AttendeeSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def event_attendee(request):
    email = request.query_params.get('email', None)  # Get the email from query parameters
    if email:
        # Find the attendee by email
        try:
            attendee = Attendee.objects.get(email=email)
        except Attendee.DoesNotExist:
            return Response({"detail": "Attendee not found."}, status=status.HTTP_404_NOT_FOUND)

        # Filter EventAttendee by the specific attendee
        event_attendees = EventAttendee.objects.filter(attendee=attendee).select_related('event')

        # Return only the event details for each EventAttendee record
        events = [EventSerializer(event_attendee.event).data for event_attendee in event_attendees]
        return Response(events)

    # If no email provided, return an error
    return Response({"detail": "Email query parameter is required."}, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def apply(request):
    serializer = EventAttendeeSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
