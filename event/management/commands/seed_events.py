import os
import random
from datetime import timedelta

import requests
from django.conf import settings
from django.core.management.base import BaseCommand
from django.utils import timezone
from faker import Faker

from event.models import Event, Attendee, EventAttendee


class Command(BaseCommand):
    help = 'Seeds the database with event, attendee, and event attendee data'

    def handle(self, *args, **kwargs):
        self.stdout.write(self.style.SUCCESS('Seeding data...'))

        fake = Faker()

        # Clear existing data
        Event.objects.all().delete()
        Attendee.objects.all().delete()
        EventAttendee.objects.all().delete()

        # Create some sample events
        events = []
        today = timezone.now().date()  # Get today's date
        for i in range(5):
            start_date = fake.date_between(start_date=today + timedelta(days=1), end_date="+30d")  # Start after today
            end_date = start_date + timedelta(days=random.randint(1, 10))  # Ensure end_date is after start_date

            # Generate a whole value for time (like 12:00:00)
            event_time = fake.random_int(min=0, max=23)  # Random hour
            time_str = f"{event_time}:00:00"  # Set minute and second to 00

            image_url = f"https://loremflickr.com/320/240/event?random={i}"
            image_filename = f"event_{i + 1}.jpg"
            image_path = os.path.join(settings.MEDIA_ROOT, 'images', image_filename)

            os.makedirs(os.path.dirname(image_path), exist_ok=True)

            response = requests.get(image_url)
            with open(image_path, 'wb') as f:
                f.write(response.content)

            event = Event.objects.create(
                name=fake.company(),
                description=fake.paragraph(nb_sentences=1),
                location=fake.address(),
                start_date=start_date,
                end_date=end_date,
                capacity=random.randint(10, 100),
                time=time_str,
                image=f"images/{image_filename}"  # Save relative path to the image
            )
            events.append(event)

        self.stdout.write(self.style.SUCCESS('Data seeded successfully!'))
