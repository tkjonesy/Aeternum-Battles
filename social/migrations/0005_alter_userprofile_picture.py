# Generated by Django 3.2.8 on 2021-10-20 22:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('social', '0004_userprofile_points'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='picture',
            field=models.ImageField(default='uploads/profile_pictures/defaultprofile.png', upload_to='uploads/profile_pictures'),
        ),
    ]
