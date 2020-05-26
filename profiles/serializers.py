from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import UserProfile

User = get_user_model()


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = UserProfile
        fields = ('id', 'email', 'username', 'is_active')


class UserListSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'id',
            'username',
            'full_name',
            'bio',
            'profile_image',
            'is_verified',
            'is_admin',
            'address',
            'created_at'
        ]

    bio = serializers.CharField(source='profile.bio')
    profile_image = serializers.URLField(source='profile.profile_image')
    is_verified = serializers.URLField(source='profile.is_verified')
    full_name = serializers.CharField(source='profile.full_name')
    address = serializers.CharField(source='profile.address')


class UserDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'id',
            'username',
            'email',
            'full_name',
            'bio',
            'profile_image',
            'is_verified',
            'address',
            'created_at'
        ]

    bio = serializers.CharField(source='profile.bio')
    profile_image = serializers.URLField(source='profile.profile_image')
    is_verified = serializers.URLField(source='profile.is_verified')
    full_name = serializers.CharField(source='profile.full_name')
    address = serializers.CharField(source='profile.address')


class UserUpdateSerializer(serializers.ModelSerializer):
    bio = serializers.CharField(source='profile.bio', allow_blank=True)
    full_name = serializers.CharField(
        source='profile.full_name',
        max_length=32,
        allow_blank=True
    )
    profile_image = serializers.URLField(
        source='profile.profile_image', allow_blank=True)

    class Meta:
        model = User
        fields = (
            'username',
            'full_name',
            'bio',
            'profile_image',
        )
        read_only_fields = ('username',)
        lookup_field = 'username'

    # Python setattr() function is used to set a value to the object's attribute.
    # It takes three arguments an object, a string, and an arbitrary value, and returns none.
    # It is helpful when we want to add a new attribute to an object and set a value to it.
    def update(self, instance, validated_data):

        # Update user profile fields
        profile_data = validated_data.pop('profile', None)
        profile = instance.profile
        for field, value in profile_data.items():
            if value:
                setattr(profile, field, value)

        # Update user fields
        for field, value in validated_data.items():
            if value:
                setattr(instance, field, value)

        profile.save()
        instance.save()
        return instance
