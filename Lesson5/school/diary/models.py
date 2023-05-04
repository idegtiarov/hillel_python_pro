from django.db import models

# Create your models here.


class Student(models.Model):
    username = models.CharField(max_length=20)
    language = models.CharField(max_length=10)
    grade = models.IntegerField()
