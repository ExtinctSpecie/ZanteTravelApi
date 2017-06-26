# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-26 15:04
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Business',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('location', models.CharField(max_length=128)),
                ('shortDescription', models.CharField(max_length=128)),
                ('longDescription', models.CharField(max_length=1024)),
                ('phoneNumber', models.CharField(max_length=15)),
                ('email', models.CharField(max_length=128)),
                ('website', models.CharField(max_length=128)),
                ('mapCoordinates', models.CharField(max_length=128)),
                ('address', models.CharField(max_length=128)),
                ('category', models.CharField(max_length=128)),
                ('type', models.CharField(max_length=128)),
                ('workingHours', models.CharField(max_length=128)),
                ('price', models.CharField(max_length=64)),
                ('usefulTip', models.CharField(max_length=128)),
                ('creditCards', models.BooleanField(default=False)),
                ('summerOnly', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='BusinessImages',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.FileField(upload_to='')),
                ('business', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Business')),
            ],
        ),
    ]
