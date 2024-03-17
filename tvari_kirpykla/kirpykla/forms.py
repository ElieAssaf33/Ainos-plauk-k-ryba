from django import forms
from django.core.validators import EmailValidator
from . import models
from django.db import models

class RegistrationForm(forms.ModelForm):
    class Meta:
        model = models.Register
        fields = ('name','email','service', 'date')
        widgets = {"date": forms.SelectDateWidget()}


