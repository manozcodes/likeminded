from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/auth/', include('authentication.urls')),
    path('api/profile/', include('profiles.urls')),
    path('api/post/', include('posts.urls')),
]
