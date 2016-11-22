# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-19 19:26
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_newsfeed'),
    ]

    operations = [
        migrations.CreateModel(
            name='NewsFeedLike',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=256)),
            ],
        ),
        migrations.RemoveField(
            model_name='newsfeed',
            name='likes_number',
        ),
        migrations.AddField(
            model_name='newsfeedlike',
            name='newsfeed',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.NewsFeed'),
        ),
    ]
