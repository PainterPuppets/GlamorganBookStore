# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-07-03 06:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='discount',
            field=models.IntegerField(default=1),
        ),
    ]
