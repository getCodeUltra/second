# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-11-02 17:45
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('letsgo', '0006_food_time'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Food',
            new_name='Cafe',
        ),
    ]
