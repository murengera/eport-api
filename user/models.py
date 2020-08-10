
from django.contrib.auth.models import AbstractUser
from django.db import models
from  .manager import  UserManager




class NullableCharField(models.CharField):
    description = " CharField that stores NULL but returns '' "

    def to_python(self, value):
        if isinstance(value, models.CharField):
            return value
        return value or ''

    def get_prep_value(self, value):
        return value or None

class myUser(AbstractUser):
    name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255, unique=True, null=True, blank=True)
    national_id = models.CharField(max_length=20, unique=True)
    phone_number = models.CharField(max_length=15, unique=True)
    username = NullableCharField(max_length=50, unique=True, null=True, blank=True)
    registered_time = models.DateTimeField(auto_now_add=True)
    reference_code = models.BigIntegerField(blank=True)

    genders = {
        ('M', 'M'),
        ('F', 'F'),
    }

    gender = models.CharField(max_length=5, choices=genders)
    date_of_birth = models.DateField()
    is_deleted = models.BooleanField(default=False)
    objects = UserManager()

    USERNAME_FIELD = 'national_id'

    def save(self, *args, **kwargs):
        if not str(self.phone_number).startswith('+'):
            raise Exception("Phone number must start with a '+'")

        if not self.reference_code:
            self.reference_code = myUser.objects.count() + 1

        super(myUser, self).save(*args, **kwargs)

    def __str__(self):
        return self.national_id


