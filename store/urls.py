from django.urls import path
from . import views

app_name = 'store'

urlpatterns = [
    path('', views.ProductListView.as_view(), name="index"),
    path('<int:id>/<slug:slug>/', views.product_detail, name="product_detail")
]