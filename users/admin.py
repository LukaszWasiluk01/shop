from django.contrib import admin

from users.views import register
from .models import Address
# Register your models here.

@admin.register(Address)
class AddressAdmin(admin.ModelAdmin):
    list_display = ['user']