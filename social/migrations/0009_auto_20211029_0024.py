# Generated by Django 3.2.8 on 2021-10-29 04:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('social', '0008_auto_20211028_1745'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='losses',
            field=models.PositiveIntegerField(default=0, verbose_name='losses'),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='wins',
            field=models.PositiveIntegerField(default=0, verbose_name='wins'),
        ),
    ]
