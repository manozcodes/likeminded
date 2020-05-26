from rest_framework import serializers
from django.contrib.auth import get_user_model
from django.utils.translation import ugettext_lazy as _
from rest_framework.validators import UniqueValidator
from django.contrib.auth import authenticate
from profiles.models import UserProfile

User = get_user_model()


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('id', 'email', 'username', 'is_active')


class UserLoginSerializer(serializers.Serializer):
    email_or_username = serializers.CharField()
    password = serializers.CharField()

    def validate(self, data):
        if '@' in data['email_or_username']:
            user = authenticate(
                email=data['email_or_username'],
                password=data['password']
            )
        else:
            user = authenticate(
                username=data['email_or_username'],
                password=data['password']
            )
        if user and user.is_active:
            return user
        raise serializers.ValidationError(
            'Incorrect credentials. Something is very wrong!')


class UserRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'id',
            'username',
            'full_name',
            'email',
            'password',
            'bio',
            'profile_image',
            'is_verified',
            'address'
        )
        extra_kwargs = {'password': {'write_only': True}, }

    username = serializers.SlugField(
        min_length=5,
        max_length=10,
        help_text=_(
            'Required. 4-10 characters. Letters, numbers, underscores or hyphens only.'
        ),
        validators=[UniqueValidator(
            queryset=User.objects.all(),
            message='has already been taken by other user'
        )],
        required=True
    )
    password = serializers.CharField(
        min_length=5,
        max_length=12,
        write_only=True,
        help_text=_(
            'Required. 5-12 characters.'
        ),
        required=True
    )
    email = serializers.EmailField(
        required=True,
        validators=[UniqueValidator(
            queryset=User.objects.all(),
            message='has already been taken by other user'
        )]
    )
    full_name = serializers.CharField(
        source='profile.full_name',
        allow_blank=False,
        max_length=60
    )
    bio = serializers.CharField(
        source='profile.bio', allow_blank=True, default='')
    profile_image = serializers.URLField(
        source='profile.profile_image', allow_blank=True, default='')
    is_verified = serializers.BooleanField(
        source='profile.is_verified', default=False)
    address = serializers.CharField(
        source='profile.address', allow_blank=True, default='')

    def create(self, validated_data):
        profile_data = validated_data.pop('profile', None)
        data = self.validated_data
        user = User.objects.create_user(
            username=data['username'],
            email=data['email'],
            password=data['password'],
        )
        user.save()

        profile_image = profile_data.get('profile_image') or None
        bio = "Say Hi to me. I'm new here"
        if not profile_image:
            profile_image = 'https://api.adorable.io/avatar/200/' + user.username
        profile = UserProfile(
            user=user,
            bio=bio,
            profile_image=profile_image,
            full_name=profile_data.get('full_name', ''),
            is_verified=profile_data.get('is_verified', False),
            address=profile_data.get('address', '')
        )
        profile.save()
        return user


class ChangePasswordSerializer(serializers.Serializer):
    old_password = serializers.CharField()
    new_password = serializers.CharField()
