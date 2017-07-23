# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-23 16:52
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0023_auto_20170718_2227'),
    ]

    operations = [
        migrations.AlterField(
            model_name='business',
            name='address',
            field=models.CharField(blank=True, max_length=128),
        ),
        migrations.AlterField(
            model_name='business',
            name='category',
            field=models.CharField(blank=True, max_length=128),
        ),
        migrations.AlterField(
            model_name='business',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2017, 7, 23, 19, 52, 24, 6908)),
        ),
        migrations.AlterField(
            model_name='business',
            name='email',
            field=models.CharField(blank=True, max_length=128),
        ),
        migrations.AlterField(
            model_name='business',
            name='mapCoordinates',
            field=models.CharField(blank=True, max_length=128),
        ),
        migrations.AlterField(
            model_name='business',
            name='phoneNumber',
            field=models.CharField(blank=True, max_length=18),
        ),
        migrations.AlterField(
            model_name='business',
            name='thumbnailURL',
            field=models.TextField(blank=True, max_length=1024),
        ),
        migrations.AlterField(
            model_name='business',
            name='type',
            field=models.CharField(blank=True, max_length=128),
        ),
        migrations.AlterField(
            model_name='business',
            name='website',
            field=models.CharField(blank=True, max_length=128),
        ),
        migrations.AlterField(
            model_name='business',
            name='workingHours',
            field=models.CharField(blank=True, max_length=128),
        ),
    ]
