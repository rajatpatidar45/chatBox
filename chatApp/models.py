from datetime import datetime
from multiprocessing.sharedctypes import Value
from tkinter.tix import Tree
from unicodedata import name
from django.db import models

# Create your models here.
class Room (models.Model):
    name=models.CharField(max_length=1000)
class message(models.Model):
    Value=models.CharField(max_length=1000)
    date=models.DateTimeField(default=datetime.now,blank=True)
    user=models.CharField(max_length=1000)
    room=models.CharField(max_length=1000)
    