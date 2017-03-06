# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-06 10:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_auto_20170306_1010'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='slug',
            field=models.SlugField(editable=False, max_length=256, unique=True),
        ),
        migrations.AlterField(
            model_name='section',
            name='slug',
            field=models.SlugField(editable=False, max_length=128, unique=True),
        ),
    ]