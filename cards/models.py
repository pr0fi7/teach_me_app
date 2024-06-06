# cards/models.py

from django.db import models

class Card(models.Model):
    question = models.CharField(max_length=100)
    answer = models.CharField(max_length=100)
    box = models.IntegerField()
    solved = models.BooleanField(default=False)
