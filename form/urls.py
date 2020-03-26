from django.contrib import admin
from django.urls import path
from .views import form, download_csv, email

urlpatterns = [
  path('', form, name='covidForm'),
  path('download-csv/', download_csv, name='download_csv'),
  path('email/', email),
]
