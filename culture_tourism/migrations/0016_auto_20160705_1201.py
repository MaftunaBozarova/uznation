# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-05 07:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('culture_tourism', '0015_auto_20160705_1132'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menu',
            name='slug',
            field=models.SlugField(max_length=250),
        ),
        migrations.AlterField(
            model_name='submenu',
            name='slug',
            field=models.SlugField(max_length=250),
        ),
    ]
