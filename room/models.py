import os

from django.db import models


def get_upload_path(instance, filename):
    return os.path.join('images', filename)


class Room(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to=get_upload_path)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'rooms'

    def __str__(self):
        return self.name



# class RoomImage(models.Model):
#     room = models.ForeignKey(Room, on_delete=models.CASCADE)
#     image = models.ImageField(upload_to='images/')
#     class Meta:
#         db_table = 'room_images'