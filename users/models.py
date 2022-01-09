from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

# Create your models here.

def validate_zip_code(value):
    if len(value) != 6:
        raise ValidationError('Wrong zip code format, should be xx-xxx')

    if value[2] != '-' and value != '':
        raise ValidationError('Wrong zip code format, should be xx-xxx')

def validate_phone_number(value):
    if len(value) != 9:
        raise ValidationError('Phone number must containt 9 numbers')
    try:
        int(value)
    except:
        raise ValidationError('Phone number must containt only numbers')

class Address(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    street= models.CharField(max_length=50, blank=True)
    house_number = models.CharField(max_length=5, blank=True)
    zip_code = models.CharField(max_length=6, blank=True, validators=[validate_zip_code])
    city = models.CharField(max_length=50, blank=True)
    phone_number = models.CharField(max_length=9,blank=True,validators=[validate_phone_number])
    objects = models.Manager()

    class Meta:
        ordering = ('user',)
        verbose_name_plural = "Addresses"