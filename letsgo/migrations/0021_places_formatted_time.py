# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-11-06 13:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('letsgo', '0020_auto_20161106_1316'),
    ]

    operations = [
        migrations.AddField(
            model_name='places',
            name='formatted_time',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
    ]
