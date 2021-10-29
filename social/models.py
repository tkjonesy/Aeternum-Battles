from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class Post(models.Model):
    objects = models.Manager()
    body = models.TextField()
    created_on = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)


class UserProfile(models.Model):
    objects = models.Manager()
    # Unchangeable username
    user = models.OneToOneField(User, primary_key=True, verbose_name='user', related_name='profile', on_delete=models.CASCADE)
    # Name can be changed by user
    name = models.CharField(max_length=30, blank=True, null=True)
    bio = models.TextField(max_length=500, blank=True)
    picture = models.ImageField(upload_to='uploads/profile_pictures', default='uploads/profile_pictures/defaultprofile.png', blank=False)
    points = models.PositiveIntegerField(default=0, verbose_name='points')
    wins = models.PositiveIntegerField(default=0, verbose_name='wins')
    losses = models.PositiveIntegerField(default=0, verbose_name='losses')
    friends = models.ManyToManyField(User, blank=True, default=None, related_name='friends')

    def modify_points(self, added_points):
        self.points += added_points
        self.save()

    def get_friends(self):
        return self.friends.all()

    def get_friends_no(self):
        return self.friends.all().count()
      
    def modify_record(self, win):
        if win:
            self.wins += 1
        elif not win:
            self.losses += 1
        self.save()


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()


class FriendRequest(models.Model):
    objects = models.Manager()
    sender = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='sender')
    receiver = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='receiver')
    is_active = models.BooleanField(blank=True, null=False, default=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    #
    # def accept(self):
    #     receiver_friend_list = FriendList.objects.get(user=self.receiver)
    #     if receiver_friend_list.exsits():
    #         receiver_friend_list.add_friend(self.sender)
    #         sender_friend_list = FriendList.objects.get(user=self.sender)
    #         if sender_friend_list.exsits():
    #             sender_friend_list.add_friend(self.receiver)
    #             self.is_active = False
    #             self.save()
    #
    # def decline(self):
    #     # declined by receiver
    #     self.is_active = False
    #     self.save()
    #
    # def cancel(self):
    #     # canceled by sender
    #     self.is_active = False
    #     self.save()


# class FriendList(models.Model):
#     user = models.OneToOneField(User, primary_key=True, verbose_name='user', related_name='profile', on_delete=models.CASCADE)
#     friends = models.ManyToManyField(settings.AUTH_USER_MODEL, blank=True, related_name='friends')
#
#     def __str__(self):
#         return self.user.username
#
#     def add_friend(self, account):
#
#         if account not in self.friends.all():
#             self.friends.add(account)
#             self.save()
#
#     def remove_friend(self, account):
#
#         if account in self.friends.all():
#             self.friends.remove(account)
#             self.save()
#
#     def unfriend(self, removee):
#         # the action of removing someone, removee is being unfriended by remover
#         remover_friends_list = self
#
#         # taking removee from remover's friend list
#         remover_friends_list.remove_friend(removee)
#
#         # taking remover from removee's  friend list
#         friends_list = FriendList.objects.get(user=removee)
#         friends_list.remove_friend(self.user)
#
#     def are_we_friends(self, friend):
#
#         if friend in self.friends.all():
#             return True
#         return False
#
#



# Create your models here.
