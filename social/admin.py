from django.contrib import admin
from .models import Post, UserProfile, FriendRequest

admin.site.register(Post)
admin.site.register(UserProfile)
admin.site.register(FriendRequest)
