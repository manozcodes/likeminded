from .serializers import (
    PostListSerializer,
    PostDetailSerializer,
    UserPostListSerializer,
    PostUpdateSerializer
)
from rest_framework import generics, views
from rest_framework.permissions import (
    AllowAny,
    IsAuthenticated,
    IsAuthenticatedOrReadOnly,
)
from authentication.permissions import IsOwnerOrAdminOrReadOnly
from django.contrib.auth import get_user_model
from .models import UserPost
from rest_framework.response import Response

User = get_user_model()


class PostListAPIView(generics.ListAPIView):
    serializer_class = PostListSerializer
    permission_classes = [AllowAny]
    queryset = UserPost.objects.all()


class PostDetailAPIView(generics.RetrieveAPIView):
    serializer_class = PostDetailSerializer
    permission_classes = [AllowAny]
    queryset = UserPost.objects.all()
    lookup_field = 'id'


class UserPostListAPIView(generics.ListAPIView):
    serializer_class = UserPostListSerializer
    permission_classes = [AllowAny]

    def get_queryset(self):
        queryset = UserPost.objects.filter(user=self.kwargs['user'])
        return queryset


class PostUpdateAPIView(generics.UpdateAPIView):
    serializer_class = PostUpdateSerializer
    permission_classes = [IsAuthenticated, IsOwnerOrAdminOrReadOnly]
    queryset = UserPost.objects.all()
    lookup_field = 'id'
