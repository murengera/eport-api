from django.db import models
from django import forms
from django.contrib.postgres.fields import JSONField,ArrayField


class ContactForm(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField()
    message=models.TextField()
    def __str__(self):
        return self.name
class Subscribe(models.Model):
    name=models.CharField(max_length=50,default='')
    email=ArrayField(models.EmailField())




  