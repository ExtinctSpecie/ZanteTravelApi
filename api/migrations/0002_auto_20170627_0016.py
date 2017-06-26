# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-26 21:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='business',
            name='thumbnail',
            field=models.FileField(default='thumbnails/none/noThumbnail.jpg', upload_to='thumbnails/'),
        ),
        migrations.AlterField(
            model_name='business',
            name='phoneNumber',
            field=models.CharField(max_length=18),
        ),
        migrations.AlterField(
            model_name='businessimages',
            name='photo',
            field=models.FileField(default='images/noImage/noImage.jpg', upload_to='images/'),
        ),
    ]
