from django.urls import path
from . import views

app_name = 'orders'

urlpatterns = [
    path('create/', views.order_create, name='order_create'),
    path('history/', views.order_history, name='order_history'),
    path('order_address/<int:id>', views.order_address_detail, name="order_address_detail")
]