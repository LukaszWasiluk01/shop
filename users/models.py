from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Address(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    street= models.CharField(max_length=50, blank=True)
    house_number = models.CharField(max_length=5, blank=True)
    zip_code = models.CharField(max_length=6, blank=True)
    city = models.CharField(max_length=50, blank=True)
    objects = models.Manager()

    class Meta:
        ordering = ('user',)
        verbose_name_plural = "Addresses"