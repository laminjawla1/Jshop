from django.contrib.auth.models import AbstractUser
from django.db import models
from phonenumber_field.modelfields import (
    PhoneNumberField,
)
from core.models import Client


class User(AbstractUser):
    class Meta:
        db_table = 'auth_user'
    
    email = models.EmailField(unique=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']


    country = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    address = models.TextField(blank=True, null=True)
    phone_number = PhoneNumberField(blank=True, null=True)