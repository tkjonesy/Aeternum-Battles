from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin
from django.views import View
from .models import Post, UserProfile, FriendRequest
from .forms import PostForm
from django.views.generic.edit import UpdateView, DeleteView


class PostListView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        posts = Post.objects.all().order_by('-created_on')
        form = PostForm()

        context = {
            'post_list': posts,
            'form': form,
        }

        return render(request, 'social/post_list.html', context)

    def post(self, request, *args, **kwargs):
        posts = Post.objects.all().order_by('-created_on')
        form = PostForm(request.POST)

        if form.is_valid():
            new_post = form.save(commit=False)
            new_post.author = request.user
            new_post.save()

            context = {
                'post_list': posts,
                'form': form,
            }

            return render(request, 'social/post_list.html', context)


class PostDetailView(LoginRequiredMixin, View):
    def get(self, request, pk, *args, **kwargs):
        post = Post.objects.get(pk=pk)

        context = {
            'post': post,
        }

        return render(request, 'social/post_detail.html', context)


class PostEditView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['body']
    template_name = 'social/post_edit.html'

    def get_success_url(self):
        pk = self.kwargs['pk']
        return reverse_lazy('post-detail', kwargs={'pk': pk})

    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    template_name = 'social/post_delete.html'
    success_url = reverse_lazy('post-list')

    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author


class ProfileView(View):
    def get(self, request, pk, *args, **kwargs):
        profile = UserProfile.objects.get(pk=pk)
        user = profile.user
        posts = Post.objects.filter(author=user).order_by('-created_on')
        friend_requests = FriendRequest.objects.filter(receiver=user.profile).order_by('-timestamp')

        context = {
            'user': user,
            'profile': profile,
            'posts': posts,
            'friend_requests': friend_requests,
        }
        return render(request, 'social/profile.html', context)


def send_request(request, pk):
    sender = request.user.profile
    receiver = UserProfile.objects.get(pk=pk)
    friend_request, created = FriendRequest.objects.get_or_create(sender=sender, receiver=receiver)
    if created:
        return HttpResponse('Friend Request Sent')
    else:
        return HttpResponse('A Friend Request Was Already Sent')


def accept_request(request, pk):
    friend_request = FriendRequest.objects.get(pk=pk)
    user1 = request.user
    user2 = friend_request.sender
    user1.friends.add(user2)
    user2.friends.add(user1)
    friend_request.delete()
    return HttpResponse('Friend Request Accepted')


class ProfileEditView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = UserProfile
    fields = ['name', 'bio', 'picture']
    template_name = 'social/profile_edit.html'

    def get_success_url(self):
        pk = self.kwargs['pk']
        return reverse_lazy('profile', kwargs={'pk': pk})

    def test_func(self):
        profile = self.get_object()
        return self.request.user == profile.user


class Leaderboard(View):
    def get(self, request, *args, **kwargs):
        users = list(UserProfile.objects.order_by('-points')[:50])

        context = {
            'users': users,
        }
        return render(request, 'social/leaderboard.html', context)
# Create your views here.
