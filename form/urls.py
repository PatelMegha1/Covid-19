from django.contrib import admin
from django.urls import path
from .views import form, success

urlpatterns = [
  path('', form, name='covidForm'),
  path('success/', success),
]
