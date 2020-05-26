from django.conf.urls import url
from django.urls import path
from knox import views as knox_views

from .api import (
    UserListAPIView,
    UserDetailAPIView,
    UserUpdateAPIView,
)

urlpatterns = [
    path('list/', UserListAPIView.as_view(), name='user-list'),
    path('<slug:username>/', UserDetailAPIView.as_view(), name='user-detail'),
    path('<slug:username>/edit/', UserUpdateAPIView.as_view(), name='user-edit'),
]
