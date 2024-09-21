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

    class Meta:
        db_table = 'events'

    def __str__(self):
        return self.name


