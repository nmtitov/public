# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-05 17:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20170305_1652'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='body',
            field=models.TextField(default='migration'),
            preserve_default=False,
        ),
    ]
