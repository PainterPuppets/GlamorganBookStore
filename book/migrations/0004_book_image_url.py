# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-07-06 06:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0003_book_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='image_url',
            field=models.URLField(blank=True, max_length=255, null=True),
        ),
    ]