# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-07-02 20:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('resources', '0008_auto_20160702_2020'),
    ]

    operations = [
        migrations.AddField(
            model_name='resource',
            name='name',
            field=models.CharField(default='Resource', max_length=255, null=True),
        ),
    ]
