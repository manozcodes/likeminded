from django.db import models
from django.contrib.auth import get_user_model
from django.conf import settings
from django.utils import timezone

User = get_user_model()


class UserPost(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='user_post')
    image = models.ImageField(upload_to='userpost/', blank=True, null=True)
    caption = models.CharField(blank=False, unique=True, max_length=500)
    like = models.BooleanField(default=0)
    published_at = models.DateTimeField(editable=False)
    updated_at = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.caption

    def save(self, *args, **kwargs):
        ''' On save, update timestamps '''
        if not self.id:
            self.published_at = timezone.now()
        self.updated_at = timezone.now()
        return super(UserPost, self).save(*args, **kwargs)
