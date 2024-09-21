import os

from django.db import models


def get_upload_path(instance, filename):
    return os.path.join('images', filename)


class Event(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    location = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField()
    capacity = models.IntegerField()
    image = models.ImageField(upload_to=get_upload_path)
    time = models.TimeField()
    attendees = models.ManyToManyField('Attendee', through='EventAttendee',related_name='events')

    class Meta:
        db_table = 'events'

    def __str__(self):
        return self.name


class Attendee(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()

    class Meta:
        db_table = 'attendees'

    def __str__(self):
        return self.name


class EventAttendee(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    attendee = models.ForeignKey(Attendee, on_delete=models.CASCADE)

    class Meta:
        db_table = 'event_attendees'
        unique_together = ('event', 'attendee')  # Ensures that an attendee can only join an event once

    def __str__(self):
        return f"{self.attendee.name} attending {self.event.name}"
