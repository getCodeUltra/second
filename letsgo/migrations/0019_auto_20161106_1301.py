# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-11-06 13:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('letsgo', '0018_remove_places_formatted_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cafe',
            name='time',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='places',
            name='time',
            field=models.DateField(null=True),
        ),
    ]
