# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-12-27 10:10
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tabby', '0011_tuser_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='base',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='tabby.Category'),
        ),
    ]
