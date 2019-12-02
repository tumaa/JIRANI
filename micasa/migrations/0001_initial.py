# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-12-02 20:40
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import pyuploadcare.dj.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0008_alter_user_username_max_length'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Business',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('business_name', models.CharField(max_length=50)),
                ('address', models.CharField(max_length=50)),
                ('category', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Hood',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('image', pyuploadcare.dj.models.ImageField()),
                ('occupants', models.CharField(max_length=50)),
                ('location_name', models.CharField(choices=[('Nairobi', 'Nairobi'), ('Kiambu', 'Kiambu'), ('Eastlands', 'Eastlands'), ('Machakos', 'Machakos'), ('Nakuru', 'Nakuru'), ('London', 'London'), ('Paris', 'Paris'), ('Vienna', 'Vienna'), ('Sydney', 'Sydney'), ('Stockholm', 'Stockholm'), ('Tokyo', 'Tokyo'), ('Hongkong', 'Hongkong'), ('Thika', 'Thika'), ('Dubai', 'Dubai'), ('New York', 'New York'), ('Los Angeles', 'Los Angeles'), ('Venice', 'Venice'), ('Cairo', 'Cairo'), ('Himalayas', 'Himalyas'), ('Antarctica', 'Antarctica'), ('Arctic', 'Arctic'), ('Fantasy', 'Fantasy'), ('Sparta', 'Sparta'), ('Mombasa', 'Mombasa')], max_length=65)),
                ('created_on', models.DateTimeField(auto_now_add=True, null=True)),
            ],
            options={
                'ordering': ['-pk'],
            },
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField(max_length=300)),
                ('title', models.CharField(max_length=65)),
                ('hood', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='micasa.Hood')),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('profile_pic', models.ImageField(blank=True, upload_to='profile/')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('bio', models.CharField(max_length=255, null=True)),
                ('full_name', models.CharField(max_length=255, null=True)),
                ('hood', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='micasa.Hood')),
            ],
        ),
        migrations.AddField(
            model_name='post',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='business',
            name='hood',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='micasa.Hood'),
        ),
        migrations.AddField(
            model_name='business',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
