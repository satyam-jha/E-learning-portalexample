from django.db import models
from django.core.validators import FileExtensionValidator
import uuid

# Create your models here.


class Question(models.Model):
    question = models.CharField(max_length=100)
    description = models.TextField(
        null=True)
    answer = models.FileField(null=True, blank=True,
                              validators=[FileExtensionValidator(allowed_extensions=['mp4'])])

    bot_id = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False)

    grade = models.ManyToManyField("Grades")
    sub = models.ManyToManyField("Subjects")

    class Meta:
        verbose_name_plural = "questions"

    def __str__(self):
        return self.question


class Grades(models.Model):
    class_choice = [
        ('6', 'sixth'),
        ('7', 'seventh'),
        ('8', 'eighth'),
        ('9', 'ninth'),
        ('10', 'tenth'),
        ('11', 'eleventh'),
        ('12', 'twelfth')
    ]
    grade = models.CharField(max_length=50, null=True, choices=class_choice)

    class Meta:
        verbose_name_plural = "Grade"

    def __str__(self):
        return self.grade


class Subjects(models.Model):
    sub_choices = [
        ('mt', 'math'),
        ('sci', 'science'),
        ('eng', 'english'),
        ('hin', 'hindi'),

    ]
    sub = models.CharField(max_length=50, null=True, choices=sub_choices)

    class Meta:
        verbose_name_plural = 'subjects'

    def __str__(self):
        return self.sub
