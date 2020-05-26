from .serializers import (
    UserSerializer,
    UserListSerializer,
    UserDetailSerializer,
    UserUpdateSerializer,
)
from rest_framework import generics, views
from rest_framework.permissions import (
    AllowAny,
    IsAuthenticated,
    IsAuthenticatedOrReadOnly,
)
from authentication.permissions import IsOwnerOrAdminOrReadOnly

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
