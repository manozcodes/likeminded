from django.conf.urls import url
from django.urls import path

from .api import (
    PostListAPIView,
    PostDetailAPIView,
    UserPostListAPIView,
    PostUpdateAPIView
)

urlpatterns = [
    path('list/', PostListAPIView.as_view(), name='post-list'),
    path('<slug:id>/', PostDetailAPIView.as_view(), name='post-detail'),
    path('user/<slug:user>/', UserPostListAPIView.as_view(),
         name='user-post-detail'),
    path('edit/<slug:id>/', PostUpdateAPIView.as_view(),
         name='post-update-detail'),

]
