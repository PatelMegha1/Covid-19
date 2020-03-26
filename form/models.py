from django.db import models
# from django.models import ModelForm
from datetime import datetime    
from django.utils import timezone

# Create your models here.

class CovidModel(models.Model):
    Name = models.fields.CharField(max_length=50)
    question1 = models.CharField(max_length=5)
    question2 = models.CharField(max_length=5)
    question3 = models.CharField(max_length=5)
    question4 = models.CharField(max_length=5)
    date = models.DateTimeField( auto_now_add = True)