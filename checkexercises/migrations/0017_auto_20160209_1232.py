# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-02-09 12:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('checkexercises', '0016_fichjs_sumary'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fichjs',
            name='sumary',
            field=models.TextField(),
        ),
    ]
