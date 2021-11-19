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


class Notifications(models.Model):
    # 1 = Friend Request | 2 = DM | 3 = Challenge
    notification_type = models.IntegerField()
    to_user = models.ForeignKey(User, related_name='notification_to', on_delete=models.CASCADE, null=True)
    from_user = models.ForeignKey(User, related_name='notification_from', on_delete=models.CASCADE, null=True)
    date = models.DateTimeField(default=timezone.now)
    user_has_seen = models.BooleanField(default=False)


# Create your models here.
