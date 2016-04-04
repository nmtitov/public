# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_post_compiled_body'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='image',
            unique_together=set([('post', 'slug')]),
        ),
    ]
