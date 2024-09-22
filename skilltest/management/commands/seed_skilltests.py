import random
from faker import Faker
from django.core.management.base import BaseCommand
from skilltest.models import SkillTest, Question, Option

class Command(BaseCommand):
    help = 'Seeds the database with SkillTest, Question, and Option data'

    def handle(self, *args, **kwargs):
        self.stdout.write(self.style.SUCCESS('Seeding data...'))

        # Initialize Faker
        fake = Faker()

        # Clear existing data
        SkillTest.objects.all().delete()
        Question.objects.all().delete()
        Option.objects.all().delete()

        # Create some Skill Tests
        for i in range(5):  # Create 5 Skill Tests
            skill_test = SkillTest.objects.create(
                name=f"Skill Test {i+1}",
                description=fake.paragraph(nb_sentences=3)
            )

            # Create some Questions for each Skill Test
            for j in range(3):  # Create 3 questions per Skill Test
                question = Question.objects.create(
                    skill_test=skill_test,
                    text=fake.sentence(nb_words=10),
                    points=random.randint(10, 30)
                )

                # Create Options for each Question
                for k in range(4):  # Create 4 options per question
                    is_correct = k == 0  # Mark the first option as correct for simplicity
                    Option.objects.create(
                        question=question,
                        text=fake.sentence(nb_words=5),
                        is_correct=is_correct
                    )

        self.stdout.write(self.style.SUCCESS('SkillTest data seeded successfully!'))
