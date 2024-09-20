from rest_framework import serializers

from room.models import Room


class RoomSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(required=True,max_length=100)
    location = serializers.CharField(required=True,max_length=100)
    created_at = serializers.DateTimeField(read_only=True)

    def create(self, validated_data):
        return Room.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.location = validated_data.get('location', instance.location)
        instance.save()
        return instance
