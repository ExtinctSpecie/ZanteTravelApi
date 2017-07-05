# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-27 23:56
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0009_somemodel_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('position', models.PositiveIntegerField(default=0)),
                ('image', models.FileField(default='images/none/noThumbnail.jpg', upload_to='images/')),
                ('business', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Business')),
            ],
        ),
    ]
