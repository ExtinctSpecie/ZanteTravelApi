# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-18 18:50
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0021_auto_20170718_2150'),
    ]

    operations = [
        migrations.AlterField(
            model_name='business',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2017, 7, 18, 21, 50, 32, 938645)),
        ),
        migrations.AlterField(
            model_name='business',
            name='thumbnailURL',
            field=models.TextField(max_length=1024),
        ),
        migrations.AlterField(
            model_name='image',
            name='imageURL',
            field=models.TextField(max_length=1024),
        ),
    ]
