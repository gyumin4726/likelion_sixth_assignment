# Generated by Django 4.2.11 on 2024-05-01 10:57

import django.contrib.auth.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_alter_profile_password'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='affiliation',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='age',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='department',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='school',
        ),
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(null=True, upload_to='profile_images/'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='nickname',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='password',
            field=models.CharField(max_length=128, verbose_name='password'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='username',
            field=models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username'),
        ),
    ]