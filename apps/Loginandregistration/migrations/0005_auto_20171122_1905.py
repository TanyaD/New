# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-11-22 19:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Loginandregistration', '0004_wish_created_by'),
    ]

    operations = [
        migrations.AlterField(
            model_name='wish',
            name='created_by',
            field=models.IntegerField(default='0', max_length=255),
        ),
    ]
