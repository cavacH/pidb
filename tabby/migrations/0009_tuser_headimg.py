# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-26 09:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tabby', '0008_category_popularity'),
    ]

    operations = [
        migrations.AddField(
            model_name='tuser',
            name='headimg',
            field=models.ImageField(null=True, upload_to='img'),
        ),
    ]
