from django.shortcuts import render, get_object_or_404
from django.http import Http404
from .models import OrderItem
from store.cart import Cart
from .forms import OrderCreateForm
from users.models import Address


# Create your views here.

def order_create(request):
    cart = Cart(request)
    if len(cart) < 1:
        raise Http404
    if request.method == 'POST':
        form = OrderCreateForm(request.POST)
        if form.is_valid():
            order = form.save()
            for item in cart:
                OrderItem.objects.create(order=order,
                                         product=item['product'],
                                         price=item['price'],
                                         quantity=item['quantity'])
            cart.clear()
            return render(request,
                          'orders/order/created.html',
                          {'order': order})
    else:
        item = Address.objects.get(user=request.user)
        if item:
            data = {
                'first_name': request.user.first_name,
                'last_name': request.user.last_name,
                'email': request.user.email,
                'phone_number': item.phone_number,
                'street': item.street,
                'house_number': item.house_number,
                'zip_code': item.zip_code,
                'city': item.city,

            }
            form = OrderCreateForm(initial = data)
        else:
            form = OrderCreateForm(instance=request.user)
        return render(request,
                      'orders/order/create.html',
                      {'cart': cart, 'form': form})