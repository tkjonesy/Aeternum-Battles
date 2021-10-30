from social.models import FriendRequest, UserProfile
from django.contrib.auth.models import User



def context_processor(request):
    if hasattr(request, 'user'):
        if hasattr(request.user, 'profile'):
            profile = request.user.profile
            print(request.user.profile)

            friend_requests = FriendRequest.objects.filter(receiver=profile).order_by('-timestamp')

            has_friend_requests = True if friend_requests else False
            print(has_friend_requests)

            data = {
                'has_friend_requests': has_friend_requests,
            }
            return data

    return {
                'has_friend_requests': False,
            }