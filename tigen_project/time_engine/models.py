from django.contrib.auth.models import User
from django.db import models

# Create your models here.
# Questions: nullable date field, how to reference the built-in User model

class Settings(models.Model):
    ical_url = models.URLField(max_length=400)

class Plan(models.Model):
    name = models.CharField(max_length=200)
    creation_date = models.DateField(auto_now_add=True)
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)
    user = models.ForeignKey(User)
    lesson_count = models.IntegerField()
    has_monday = models.BooleanField()
    has_tuesday = models.BooleanField()
    has_wednesday = models.BooleanField()
    has_thursday = models.BooleanField()
    has_friday = models.BooleanField()
    has_saturday = models.BooleanField()
    has_sunday = models.BooleanField()


class PlanResults(models.Model):
    lesson_no = models.IntegerField()
    lesson_date = models.DateField()
    plan = models.ForeignKey(Plan)

