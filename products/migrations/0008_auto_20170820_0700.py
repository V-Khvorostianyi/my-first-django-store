# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-20 04:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0007_productimage_is_main'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productimage',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='productimage',
            name='is_main',
            field=models.BooleanField(default=False),
        ),
    ]
