from rest_framework import serializers

from event.models import Event


class EventSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField()
    description = serializers.CharField()
    location = serializers.CharField()
    start_date = serializers.DateField()
    end_date = serializers.DateField()
    capacity = serializers.IntegerField()
    time = serializers.TimeField()

    class Meta:
        model = Event
        fields = ('id', 'name', 'description', 'location', 'start_date', 'end_date', 'capacity', 'time')

    def create(self, validated_data):
        return Event.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.description = validated_data.get('description', instance.description)
        instance.location = validated_data.get('location', instance.location)
        instance.start_date = validated_data.get('start_date', instance.start_date)
        instance.end_date = validated_data.get('end_date', instance.end_date)
        instance.capacity = validated_data.get('capacity', instance.capacity)
        instance.time = validated_data.get('time', instance.time)
        instance.save()
        return instance