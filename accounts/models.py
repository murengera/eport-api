from django.db import models

from django.contrib.auth.models import User


class ContactUs(models.Model):

    name=models.ForeignKey(User,on_delete=models.CASCADE)
    email=models.EmailField()
    message = models.TextField()
    def __str__(self):
        return str((self.name.username,self.message))


