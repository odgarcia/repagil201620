# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-11-14 22:24
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Artist',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=1000, null=True)),
                ('last_name', models.CharField(max_length=1000, null=True)),
                ('avatar', models.ImageField(blank=True, null=True, upload_to='static/avatars/')),
                ('name_artistic', models.CharField(blank=True, max_length=50)),
                ('email', models.CharField(max_length=1000)),
                ('city', models.CharField(blank=True, max_length=50)),
                ('country', models.CharField(blank=True, max_length=50)),
                ('birth_date', models.DateField(blank=True, null=True)),
                ('userId', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60)),
            ],
        ),
        migrations.CreateModel(
            name='Collection',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60)),
            ],
        ),
        migrations.CreateModel(
            name='Piece',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60)),
                ('url', models.CharField(blank=True, max_length=100, null=True)),
                ('image_cover', models.CharField(blank=True, max_length=100, null=True)),
                ('duration', models.CharField(blank=True, max_length=100, null=True)),
                ('lyrics', models.TextField(blank=True, null=True)),
                ('artist', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='api.Artist')),
                ('category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='api.Category')),
            ],
        ),
        migrations.CreateModel(
            name='PieceCollection',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('collection', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Collection')),
                ('piece', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Piece')),
            ],
        ),
        migrations.CreateModel(
            name='PieceLike',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=256)),
                ('piece', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Piece')),
            ],
        ),
        migrations.CreateModel(
            name='Rank',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('piece_name', models.CharField(max_length=256)),
                ('likes_number', models.IntegerField()),
            ],
        ),
    ]
