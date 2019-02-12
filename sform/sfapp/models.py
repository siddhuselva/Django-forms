from django.db import models
from django import forms

class Allusers(models.Model):
    uname = models.CharField("USERNAME", max_length=20,default='xxx')
    uemail = models.CharField("EMAIL", max_length=50,default='xxx')
    upswd = models.CharField("PASSWORD", max_length=20,default='xxx',widgets = forms.PasswordInput())


