# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-27 23:17
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_auto_20170627_0044'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='businessimages',
            name='business',
        ),
    ]