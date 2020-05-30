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

    def __str__(self):
        return self.user.username


class UserFollowing(models.Model):
    follower_user_id = models.ForeignKey(
        User, related_name="following", on_delete=models.CASCADE
    )
    following_user_id = models.ForeignKey(
        User, related_name="followers", on_delete=models.CASCADE
    )
    created = models.DateTimeField(auto_now_add=True, db_index=True)

    class Meta:
        unique_together = ("follower_user_id", "following_user_id")
        ordering = ["-created"]

    def __str__(self):
        return f"{self.follower_user_id} follows {self.following_user_id}"
