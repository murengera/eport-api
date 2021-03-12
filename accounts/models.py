from django.db import models


class ContactUs(models.Model):


    email=models.EmailField()
    message = models.TextField()



