from social.models import FriendRequest, UserProfile


def context_processor(request):
    if hasattr(request, 'user'):
        if hasattr(request.user, 'profile'):
            profile = request.user.profile

            friend_requests = FriendRequest.objects.filter(receiver=profile).order_by('-timestamp')

            has_friend_requests = True if friend_requests else False

            data = {
                'friend_requests': has_friend_requests,
            }
            return data

    return {
                'friend_requests': False,
            }