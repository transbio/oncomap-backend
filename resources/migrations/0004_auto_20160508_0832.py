# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-08 08:32
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('resources', '0003_auto_20160507_1004'),
    ]

    operations = [
        migrations.RenameField(
            model_name='voting',
            old_name='created',
            new_name='created_date',
        ),
    ]
