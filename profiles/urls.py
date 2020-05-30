from django.conf.urls import url
from django.urls import path
from knox import views as knox_views
from rest_framework.routers import SimpleRouter

from .api import (
    UserListAPIView,
    UserDetailAPIView,
    UserUpdateAPIView,
    UserFollowingViewSet
)

router = SimpleRouter()
router.register("follow", UserFollowingViewSet, basename="user-follow")

urlpatterns = [
    path('list/', UserListAPIView.as_view(), name='user-list'),
    path('<slug:username>', UserDetailAPIView.as_view(), name='user-detail'),
    path('<slug:username>/edit/', UserUpdateAPIView.as_view(), name='user-edit'),

]

urlpatterns += router.urls
