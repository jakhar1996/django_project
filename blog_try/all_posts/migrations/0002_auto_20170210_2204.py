# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-10 22:04
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('all_posts', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='posts',
            name='slug',
        ),
        migrations.AddField(
            model_name='posts',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]