from audioop import reverse
import email
from unicodedata import name
from django.db import models
from django.urls import reverse

class ContactMe(models.Model):
    name = models.CharField(max_length=150)
    email = models.EmailField()
    subject =models.CharField(max_length=150)
    menssage = models.CharField(max_length=150)
    def get_absolute_url(self):
        return reverse('home')
