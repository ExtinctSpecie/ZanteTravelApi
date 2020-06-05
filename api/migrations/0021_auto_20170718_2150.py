# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-18 18:50
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0020_auto_20170717_1922'),
    ]

    operations = [
        migrations.AddField(
            model_name='business',
            name='thumbnailURL',
            field=models.TextField(default='', max_length=1024),
        ),
        migrations.AddField(
            model_name='image',
            name='imageURL',
            field=models.TextField(default='', max_length=1024),
        ),
        migrations.AlterField(
            model_name='business',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2017, 7, 18, 21, 50, 14, 305593)),
        ),
    ]