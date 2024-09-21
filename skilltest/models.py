from django.db import models


class SkillTest(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    class Meta:
        db_table = 'skill_tests'

    def __str__(self):
        return self.name


class Question(models.Model):
    skill_test = models.ForeignKey(SkillTest, related_name='questions', on_delete=models.CASCADE)
    text = models.CharField(max_length=1000)
    points = models.IntegerField(default=20)

    class Meta:
        db_table = 'questions'

    def __str__(self):
        return self.text


class Option(models.Model):
    question = models.ForeignKey(Question, related_name='options', on_delete=models.CASCADE)
    text = models.CharField(max_length=1000)
    is_correct = models.BooleanField(default=False)

    class Meta:
        db_table = 'options'

    def __str__(self):
        return f"{self.text} (Correct: {self.is_correct})"