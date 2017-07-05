# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-04 20:09
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0013_business_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='business',
            name='groupID',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='business',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2017, 7, 4, 23, 9, 39, 49462)),
        ),
    ]
