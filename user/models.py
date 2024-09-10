from django.contrib.auth.models import AbstractUser
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


class User(AbstractUser):
    username = None
    name = models.CharField(max_length=50, blank=True, null=True)
    email = models.EmailField(
        max_length=70, unique=True)
    phone_number = PhoneNumberField(unique=True, blank=True)
    
    # Default fields
    is_active = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']
    def __str__(self):
        return self.email


class Role(models.Model):
    name = models.CharField(max_length=50, unique=True)
    users = models.ManyToManyField(User, related_name='roles')
    
    def __str__(self):
        return self.name
