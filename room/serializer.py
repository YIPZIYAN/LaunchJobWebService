from PIL.EpsImagePlugin import field
from rest_framework import serializers

from room.models import Room, RoomGallery


class RoomGallerySerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    image = serializers.ImageField(required=True)
    room = serializers.PrimaryKeyRelatedField(queryset=Room.objects.all())  # Associate image with a room

    class Meta:
        model = RoomGallery
        fields = ['id', 'image', 'room']

    def create(self, validated_data):
        return RoomGallery.objects.create(**validated_data)


class RoomSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    owner = serializers.CharField(required=True)
    email = serializers.EmailField(required=True)
    contact = serializers.CharField(required=True)
    name = serializers.CharField(required=True,max_length=100)
    location = serializers.CharField(required=True,max_length=100)
    price = serializers.IntegerField(required=True)
    type = serializers.CharField(required=True,max_length=100)
    description = serializers.CharField(required=True)
    thumbnail = serializers.ImageField(required=True)
    tags = serializers.CharField(required=True,max_length=100)
    galleries = RoomGallerySerializer(many=True, read_only=True)
    created_at = serializers.DateTimeField(read_only=True)

    class Meta:
        model = Room
        fields = ['id', 'name', 'location', 'description', 'thumbnail', 'galleries', 'created_at']

    def create(self, validated_data):
        return Room.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.location = validated_data.get('location', instance.location)
        instance.save()
        return instance
