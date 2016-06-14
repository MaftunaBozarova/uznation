# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('culture_tourism', '0002_mainarticle_slide'),
    ]

    operations = [
        migrations.RenameField(
            model_name='mainarticle',
            old_name='article_title',
            new_name='article_title1',
        ),
        migrations.RenameField(
            model_name='mainarticle',
            old_name='b_subtext',
            new_name='b_box',
        ),
        migrations.RenameField(
            model_name='mainarticle',
            old_name='b_title',
            new_name='b_tild',
        ),
        migrations.RemoveField(
            model_name='mainarticle',
            name='article_body',
        ),
        migrations.RemoveField(
            model_name='mainarticle',
            name='article_photo',
        ),
        migrations.RemoveField(
            model_name='mainarticle',
            name='b_number',
        ),
        migrations.AddField(
            model_name='mainarticle',
            name='article_body1',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='mainarticle',
            name='article_body2',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='mainarticle',
            name='article_photo1',
            field=models.ImageField(upload_to='main_article/', blank=True),
        ),
        migrations.AddField(
            model_name='mainarticle',
            name='article_photo2',
            field=models.ImageField(upload_to='main_article/', blank=True),
        ),
        migrations.AddField(
            model_name='mainarticle',
            name='article_title2',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AddField(
            model_name='mainarticle',
            name='b_word1',
            field=models.CharField(null=True, blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='mainarticle',
            name='b_word2',
            field=models.CharField(null=True, blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='mainarticle',
            name='b_word3',
            field=models.CharField(null=True, blank=True, max_length=100),
        ),
    ]
