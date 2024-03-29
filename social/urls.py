from django.urls import path
from .views import PostListView, PostDetailView, PostEditView, PostDeleteView, ProfileView, ProfileEditView, Leaderboard, send_request, accept_request, UserSearch, Friendlist, FriendNotification, RemoveNotification

urlpatterns = [
    path('', PostListView.as_view(), name='post-list'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/edit/<int:pk>/', PostEditView.as_view(), name='post-edit'),
    path('post/delete/<int:pk>/', PostDeleteView.as_view(), name='post-delete'),
    path('profile/<int:pk>/', ProfileView.as_view(), name='profile'),
    path('profile/edit/<int:pk>/', ProfileEditView.as_view(), name='profile-edit'),
    path('profile/<int:pk>/friends/', Friendlist.as_view(), name='friend-list'),
    path('leaderboard/', Leaderboard.as_view(), name='leaderboard'),
    path('add-friend/<int:pk>', send_request, name='add-friend'),
    path('accept/<int:pk>', accept_request, name='accept-request'),
    path('search/', UserSearch.as_view(), name='profile-search'),
    path('notification/<int:notification_pk>/profile/<int:to_user_pk>', FriendNotification.as_view(), name='friend-notification'),
    path('notification/delete/<int:notification_pk>', RemoveNotification.as_view(), name='remove-notification'),

]
