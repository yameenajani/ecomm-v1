# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2020-01-17 05:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_emailactivation'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='is_seller',
            field=models.BooleanField(default=False),
        ),
    ]
