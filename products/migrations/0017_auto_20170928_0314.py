# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-28 00:14
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0016_auto_20170824_2123'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='price',
            new_name='price_per_item',
        ),
    ]
