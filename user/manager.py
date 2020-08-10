
from django.contrib.auth.models import UserManager as UManager


class UserManager(UManager):
    """
    Customises Django User Manager, by replacing the required username with national_id,
    Creating users require the national_id not username.
    """

    def _create_user(self, phone_number, national_id,  password, **extra_fields):
        """
        Creates and saves a User with the given phone_number, national_id and password.
        """
        if not national_id:
            raise ValueError('The given national_id must be set')
        if not phone_number:
            raise ValueError('The given phone number must be set')
        user = self.model(national_id=national_id, phone_number=phone_number, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, national_id, phone_number=None, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(phone_number=phone_number, national_id=national_id, password=password, **extra_fields)

    def create_superuser(self, national_id, password, phone_number, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(phone_number=phone_number, national_id=national_id, password=password, **extra_fields)
