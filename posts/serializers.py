from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import UserPost

User = get_user_model()


class PostListSerializer(serializers.ModelSerializer):

    class Meta:
        model = UserPost
        # fields = [
        #     'id',
        #     'username',
        #     'image',
        #     'caption',
        #     'like',
        #     'published_at',
        #     'updated_at',
        # ]
        fields = '__all__'

    # image = serializers.ImageField(source='user_post.image')
    # caption = serializers.CharField(source='user_post.caption')
    # like = serializers.BooleanField(source='user_post.like')
    # published_at = serializers.DateTimeField(source='user_post.published_at')
    # updated_at = serializers.DateTimeField(source='user_post.updated_at')


class PostDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserPost
        fields = [
            'id',
            'user',
            'image',
            'caption',
            'like',
            'published_at',
            'updated_at',
        ]


class UserPostListSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserPost
        fields = [
            'id',
            'user',
            'image',
            'caption',
            'like',
            'published_at',
            'updated_at',
        ]


class PostUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserPost
        fields = [
            'image',
            'caption',
        ]
