# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2015-12-17 16:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('checkexercises', '0003_fichjs'),
    ]

    operations = [
        migrations.RenameField(
            model_name='fichjs',
            old_name='content',
            new_name='analisis',
        ),
        migrations.AddField(
            model_name='studentexercise',
            name='analizado',
            field=models.BooleanField(default=False),
        ),
    ]
