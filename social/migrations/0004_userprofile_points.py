# Generated by Django 3.2.8 on 2021-10-20 01:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('social', '0003_userprofile'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='points',
            field=models.PositiveIntegerField(default=0, verbose_name='points'),
        ),
    ]