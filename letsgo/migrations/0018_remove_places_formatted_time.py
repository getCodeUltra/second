# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-11-06 12:59
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('letsgo', '0017_auto_20161106_1258'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='places',
            name='formatted_time',
        ),
    ]
