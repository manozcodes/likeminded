from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class UserProfile(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, related_name='profile')
    full_name = models.CharField(max_length=255, blank=False)
    is_verified = models.BooleanField(default=False)
    address = models.CharField(max_length=255, blank=True)
    profile_image = models.URLField(default='', blank=True)
    bio = models.TextField(max_length=2000, blank=True)
    followers = models.IntegerField(default=0)
    following = models.IntegerField(default=0)

    def __str__(self):
        return self.user.username
