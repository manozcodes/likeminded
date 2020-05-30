from django.contrib import admin
from .models import UserProfile, UserFollowing

admin.site.register(UserProfile)
admin.site.register(UserFollowing)
