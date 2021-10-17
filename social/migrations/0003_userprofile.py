# Generated by Django 3.2.8 on 2021-10-14 05:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('social', '0002_post_body'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, related_name='profile', serialize=False, to='auth.user', verbose_name='user')),
                ('name', models.CharField(blank=True, max_length=30, null=True)),
                ('bio', models.TextField(blank=True, max_length=500)),
                ('picture', models.ImageField(blank=True, default='uploads/profile_pictures/defaultprofile.png', upload_to='uploads/profile_pictures')),
            ],
        ),
    ]
