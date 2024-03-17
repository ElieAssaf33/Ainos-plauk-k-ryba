from django.db import models
from django import forms
from django.contrib.admin import widgets

class Register(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    service = models.CharField(max_length=100)
    date = models.DateField(null =True)


