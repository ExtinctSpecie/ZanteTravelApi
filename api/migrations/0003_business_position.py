# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-26 21:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_auto_20170627_0016'),
    ]

    operations = [
        migrations.AddField(
            model_name='business',
            name='position',
            field=models.IntegerField(default=5, unique=True),
        ),
    ]
