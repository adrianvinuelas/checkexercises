# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-02-16 16:36
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('checkexercises', '0026_studentexercise_namestudent'),
    ]

    operations = [
        migrations.AddField(
            model_name='studentexercise',
            name='urlAvatar',
            field=models.CharField(default=datetime.datetime(2016, 2, 16, 16, 36, 53, 488796, tzinfo=utc), max_length=500),
            preserve_default=False,
        ),
    ]
