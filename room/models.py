import os

from django.db import models


def get_upload_path(instance, filename):
    return os.path.join('images', filename)

class Room(models.Model):
    owner = models.CharField(max_length=100)
    email = models.EmailField()
    contact = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    price = models.IntegerField()
    description = models.TextField()
    type = models.CharField(max_length=100)
    thumbnail = models.ImageField(upload_to=get_upload_path)
    tags = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'rooms'

    def __str__(self):
        return self.name



class RoomGallery(models.Model):
    room = models.ForeignKey(Room, on_delete=models.CASCADE,related_name='galleries')
    image = models.ImageField(upload_to=get_upload_path)
    class Meta:
        db_table = 'room_galleries'

    def __str__(self):
        return self.image.path
