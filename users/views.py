from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import RegisterForm, AddressForm, PersonalInfoForm
from .models import Address
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required
# Create your views here.

def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.first_name = user.first_name.capitalize()
            user.last_name = user.last_name.capitalize()
            user.save()
            Address.objects.create(user = user)
            username= form.cleaned_data.get("username")
            messages.success(request,f'Welcome {username}, your account is created')
            return redirect('login')
    else:
        form= RegisterForm()
    return render(request,'users/register.html', {'form':form})

@login_required
def address(request):
    if request.method == "POST":
        form = AddressForm(request.POST)
        if form.is_valid():
            address = form.save(commit=False)
            address.user = request.user
            address.save()
            return redirect('users:address')
    else:
        item = get_object_or_404(Address, user=request.user)
        form = AddressForm(instance=item)
    return render(request,'users/address.html', {'form':form})

@login_required
def personal_info(request):
    if request.method == "POST":
        form = PersonalInfoForm(data=request.POST, instance=request.user)
        if form.is_valid():
            user = form.save(commit=False)
            user.first_name = user.first_name.capitalize()
            user.last_name = user.last_name.capitalize()
            user.save()
            return redirect('users:personal_info')
    else:
        form = PersonalInfoForm(instance=request.user)
    return render(request,'users/personal_info.html', {'form':form})

