import email
from unicodedata import name
from django.db import models

class ContactMe(models.Model):
    name = models.CharField(max_length=150)
    email = models.EmailField()
    subject =models.CharField(max_length=150)
    menssage = models.CharField(max_length=150)
