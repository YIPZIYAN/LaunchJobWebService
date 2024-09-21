from rest_framework import serializers

from event.models import Event, Attendee, EventAttendee


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

    class Meta:
        model = Event
        fields = ('id', 'name', 'description', 'location', 'start_date', 'end_date', 'capacity', 'time', 'image')

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
        instance.save()
        return instance


class AttendeeSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(required=True, max_length=100)
    email = serializers.EmailField(required=True, max_length=100)

    class Meta:
        model = Attendee
        fields = ('id', 'name', 'email')

    def create(self, validated_data):
        return Attendee.objects.create(**validated_data)


class EventAttendeeSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    event_id = serializers.PrimaryKeyRelatedField(queryset=Event.objects.all(), source='event')
    email = serializers.EmailField(required=True, write_only=True)
    name = serializers.CharField(required=True, max_length=100, write_only=True)

    class Meta:
        model = EventAttendee
        fields = ('id', 'event_id', 'email', 'name')

    def create(self, validated_data):
        event = validated_data.get('event')
        name = validated_data.get('name')
        email = validated_data.get('email')

        if event.capacity <= 0:
            raise serializers.ValidationError("The event has reached its capacity.")

        attendee, created = Attendee.objects.get_or_create(
            email=email,
            defaults={'name': name}
        )

        if EventAttendee.objects.filter(event=event, attendee=attendee).exists():
            raise serializers.ValidationError("This attendee is already registered for this event.")

        event_attendee = EventAttendee.objects.create(event=event, attendee=attendee)

        event.capacity -= 1
        event.save()

        return event_attendee
