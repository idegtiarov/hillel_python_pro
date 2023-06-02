from django.contrib.auth.models import User
from django.db import models

# Create your models here

class BaseWeekDay(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    day = models.CharField(max_length=20)

    class Meta:
        abstract = True

    def __str__(self):
        return f"Week day: {self.day}"

class WeekDay(BaseWeekDay):
    ...

class WorkDay(WeekDay):
    working_hours = models.CharField(max_length=20)

class WeekEnd(WeekDay):
    events = models.CharField(max_length=100)


class Note(models.Model):
    week_day = models.ForeignKey(WeekDay, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    msg = models.CharField(max_length=250)
