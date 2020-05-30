from .serializers import (
    UserSerializer,
    UserListSerializer,
    UserDetailSerializer,
    UserUpdateSerializer,
    UserFollowingSerializer
)
from rest_framework import generics, views, mixins, viewsets
from rest_framework.permissions import (
    AllowAny,
    IsAuthenticated,
    IsAuthenticatedOrReadOnly,
)
from authentication.permissions import IsOwnerOrAdminOrReadOnly
from django.contrib.auth import get_user_model
from .models import UserFollowing

User = get_user_model()


class UserListAPIView(generics.ListAPIView):
    serializer_class = UserListSerializer
    permission_classes = [AllowAny]
    queryset = User.objects.all()


class UserDetailAPIView(generics.RetrieveAPIView):
    serializer_class = UserDetailSerializer
    permission_classes = [AllowAny]
    queryset = User.objects.all()
    lookup_field = 'username'


class UserUpdateAPIView(generics.UpdateAPIView):
    serializer_class = UserUpdateSerializer
    permission_classes = [IsOwnerOrAdminOrReadOnly]
    queryset = User.objects.all()
    lookup_field = 'username'


class UserFollowingViewSet(
    mixins.CreateModelMixin, mixins.DestroyModelMixin, viewsets.GenericViewSet
):
    permission_classes = (AllowAny,)
    serializer_class = UserFollowingSerializer
    queryset = UserFollowing.objects.all()
