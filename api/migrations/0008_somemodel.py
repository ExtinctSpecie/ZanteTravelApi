# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-27 23:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0007_delete_businessimages'),
    ]

    operations = [
        migrations.CreateModel(
            name='SomeModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('position', models.PositiveIntegerField(default=0)),
                ('name', models.CharField(max_length=128)),
                ('location', models.CharField(max_length=128)),
            ],
        ),
    ]
