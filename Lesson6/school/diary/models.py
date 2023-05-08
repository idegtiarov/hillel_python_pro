from django.db import models

# Create your models here.


class WeekDay(models.Model):
    title = models.CharField(max_length=20)
    note = models.CharField(max_length=250)

    def __str__(self):
        return f"Week day: {self.title}, day note: {self.note}"

