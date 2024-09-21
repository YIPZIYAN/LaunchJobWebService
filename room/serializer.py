from rest_framework import serializers

from room.models import Room, RoomGallery


class RoomGallerySerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    image = serializers.ImageField(required=True)

    class Meta:
        model = RoomGallery
        fields = ('id', 'image')
        def create(self, validated_data):
            return RoomGallery.objects.create(**validated_data)

class RoomSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(required=True,max_length=100)
    location = serializers.CharField(required=True,max_length=100)
    description = serializers.CharField(required=True)
    image = serializers.ImageField(required=True)
    room_gallery = serializers.StringRelatedField(many=True)
    created_at = serializers.DateTimeField(read_only=True)

    class Meta:
        model = Room
        fields = ['id', 'name', 'location', 'description', 'image', 'created_at']

    def create(self, validated_data):
        return Room.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.location = validated_data.get('location', instance.location)
        instance.save()
        return instance
