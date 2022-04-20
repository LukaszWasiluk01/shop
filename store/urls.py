from django.urls import path
from . import views

app_name = 'store'

urlpatterns = [
    path('', views.ProductListView.as_view(), name="index"),
    path('<slug:slug>/', views.ProductListView.as_view(), name="index_filtered"),
    path('<int:id>/<slug:slug>/', views.product_detail, name="product_detail"),
    path('cart/', views.cart_detail, name='cart_detail'),
    path('cart/add/<int:product_id>/', views.cart_add, name='cart_add'),
    path('cart/remove/<int:product_id>/', views.cart_remove, name='cart_remove'),
]