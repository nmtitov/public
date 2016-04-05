# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-05 00:53
from __future__ import unicode_literals

from django.db import migrations, models


def create_sections(apps, schema_editor):
    section = apps.get_model("blog", "Section")
    try:
        section.objects.create(title="Production")
        section.objects.create(title="Tutorials")
    except Exception:
        pass


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_section_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='section',
            name='slug',
            field=models.CharField(max_length=32, unique=True),
        ),
        migrations.RunPython(create_sections),
    ]
