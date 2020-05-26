from .serializers import (
    UserSerializer,
    UserListSerializer,
    UserDetailSerializer,
    UserUpdateSerializer,
)
from django.contrib.auth import get_user_model, update_session_auth_hash
from rest_framework import generics, views
from rest_framework.response import Response
from knox.models import AuthToken
from rest_framework.permissions import (
    AllowAny,
    IsAuthenticated,
    IsAuthenticatedOrReadOnly,
)
from authentication.permissions import IsOwnerOrAdminOrReadOnly
from rest_framework.status import HTTP_400_BAD_REQUEST

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
