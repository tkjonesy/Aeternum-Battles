from django.contrib import admin
from .models import Post, UserProfile, FriendRequest, Notifications

admin.site.register(Post)
admin.site.register(UserProfile)
admin.site.register(FriendRequest)
admin.site.register(Notifications)
