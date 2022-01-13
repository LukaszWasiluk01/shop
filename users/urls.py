from django.urls import path
from . import views

app_name = 'users'

urlpatterns = [
    path('register/', views.register, name="register"),
    path('address/', views.address, name="address"),
    path('personal_info/', views.personal_info, name="personal_info")
]