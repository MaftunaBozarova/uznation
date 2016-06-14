# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('culture_tourism', '0003_auto_20160613_1316'),
    ]

    operations = [
        migrations.AddField(
            model_name='mainarticle',
            name='article_body3',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='mainarticle',
            name='article_photo3',
            field=models.ImageField(blank=True, upload_to='main_article/'),
        ),
        migrations.AddField(
            model_name='mainarticle',
            name='article_title3',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AddField(
            model_name='mainarticle',
            name='b_image',
            field=models.ImageField(blank=True, upload_to='main_article/'),
        ),
    ]
