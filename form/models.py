from django.db import models
from django.models import ModelForm


# Create your models here.

class CovidModel(models.Model):
    firstName = models.fields.CharField(max_length=50)
    lastname = models.fields.CharField(max_length=50)
    question1 = models.fieldsser5
    question2 = models.CheckboxInput
    question3 = models.CheckboxInput
    question4 = models.CheckboxInput

 