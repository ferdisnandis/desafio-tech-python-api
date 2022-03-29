from tkinter import CASCADE
from unicodedata import name
from django.db import models

# Create your models here.

class Region(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Fruits(models.Model):
    name = models.CharField(max_length=50)
    region = models.ForeignKey(Region, on_delete=models.CASCADE, related_name='region')

    def __str__(self):
        return self.name