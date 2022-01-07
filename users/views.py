from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import RegisterForm, AddressForm
from .models import Address
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required
# Create your views here.

def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            Address.objects.create(user = user)
            username= form.cleaned_data.get("username")
            messages.success(request,f'Welcome {username}, your account is created')
            return redirect('users:login')
    else:
        form= RegisterForm()
    return render(request,'registration/register.html', {'form':form})

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