# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-02-29 16:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('checkexercises', '0035_studentexercise_firstfich'),
    ]

    operations = [
        migrations.AddField(
            model_name='studentexercise',
            name='hayfirstfich',
            field=models.BooleanField(default=False),
        ),
    ]
