from django.contrib import admin
from .models import Post, UserProfile

admin.site.register(Post)
admin.site.register(UserProfile)


# class FriendListAdmin(admin.ModelAdmin):
#     list_filter = ['user']
#     list_display = ['user']
#     search_fields = ['user']
#     readonly_fields = ['user']
#
#     class Meta:
#         model = FriendList
#
#
# admin.site.register(FriendList)


# class FriendRequestAdmin(admin.ModelAdmin):
#     list_filter = ['sender', 'receiver'],
#     list_display = ['sender', 'receiver'],
#     search_fields = ['sender__username', 'receiver__username']
#
#     class Meta:
#         model = FriendRequest
#
#
# admin.site.register(FriendRequest)
