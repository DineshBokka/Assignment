# Level_1.py

from django.db import models

class Teacher(models.Model):
    name = models.CharField(max_length=100)
    students = models.ManyToManyField('Student', related_name='teachers')

class Student(models.Model):
    name = models.CharField(max_length=100)
