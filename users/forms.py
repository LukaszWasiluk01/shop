from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Address

class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)
 
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']

User._meta.get_field('email')._unique = True

class AddressForm(forms.ModelForm):
    class Meta:
        model = Address
        fields = ['street', 'house_number', 'zip_code', 'city', 'phone_number']