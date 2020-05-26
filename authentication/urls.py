from django.conf.urls import url
from django.urls import include, path
from django.contrib import admin
from knox import views as knox_views

from .api import (
    UserRegisterAPIView,
    UserLoginAPIView,
    ChangePasswordView,
)

urlpatterns = [
    path('register/', UserRegisterAPIView.as_view(), name='user-register'),
    path('login/', UserLoginAPIView.as_view(), name='user-login'),
    path('logout/', knox_views.LogoutView.as_view(), name='knox_logout'),
    path('change-password/',
         ChangePasswordView.as_view(), name='change-password'),
]
