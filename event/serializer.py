from rest_framework import serializers

from event.models import Event


class EventSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(required=True, max_length=100)
    description = serializers.CharField(required=True, max_length=1000)
    location = serializers.CharField(required=True, max_length=100)
    start_date = serializers.DateField(required=True)
    end_date = serializers.DateField(required=True)
    capacity = serializers.IntegerField(required=True)
    time = serializers.TimeField(required=True)
    image = serializers.ImageField(required=True)
    created_date = serializers.DateField(required=True)

    class Meta:
        model = Event
        fields = ('id', 'name', 'description', 'location', 'start_date', 'end_date', 'capacity', 'time', 'image',
                  'created_date')

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
        instance.image = validated_data.get('image', instance.image)
        instance.created_date = validated_data.get('created_date', instance.created_date)
        instance.save()
        return instance
