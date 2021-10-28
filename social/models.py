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
    user = models.OneToOneField(User, primary_key=True, verbose_name='user', related_name='profile', on_delete=models.CASCADE)
    name = models.CharField(max_length=30, blank=True, null=True)
    bio = models.TextField(max_length=500, blank=True)
    picture = models.ImageField(upload_to='uploads/profile_pictures', default='uploads/profile_pictures/defaultprofile.png', blank=False)
    points = models.PositiveIntegerField(default=0, verbose_name='points')
    wins = models.PositiveIntegerField(default=0, verbose_name='wins')
    losses = models.PositiveIntegerField(default=0, verbose_name='losses')

    def modify_points(self, added_points):
        self.points += added_points
        self.save()

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


# Create your models here.
