# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('culture_tourism', '0005_mostvisited'),
    ]

    operations = [
        migrations.AddField(
            model_name='generalinfo',
            name='info_slug',
            field=models.SlugField(max_length=200, blank=True),
        ),
        migrations.AddField(
            model_name='generalinfo',
            name='is_small_text',
            field=models.BooleanField(default=True),
        ),
    ]
