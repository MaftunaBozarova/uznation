# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import ckeditor.fields
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('name', models.CharField(blank=True, max_length=150)),
                ('email', models.EmailField(blank=True, max_length=254)),
                ('comment', ckeditor.fields.RichTextField()),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('active', models.BooleanField(default=False)),
            ],
            options={
                'ordering': ('created',),
            },
        ),
        migrations.CreateModel(
            name='Gallery',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('category', models.CharField(blank=True, max_length=50)),
                ('photo', models.ImageField(upload_to='gallery/')),
                ('description', ckeditor.fields.RichTextField()),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Library',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('lib_name', models.CharField(blank=True, max_length=255)),
                ('lib_photo', models.ImageField(upload_to='library/', blank=True)),
                ('lib_file', models.FileField(upload_to='library/', blank=True)),
                ('lib_description', ckeditor.fields.RichTextField()),
                ('lib_created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='MainArticle',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('b_word1', models.CharField(null=True, blank=True, max_length=100)),
                ('b_word2', models.CharField(null=True, blank=True, max_length=100)),
                ('b_word3', models.CharField(null=True, blank=True, max_length=100)),
                ('b_tild', models.CharField(null=True, blank=True, max_length=200)),
                ('b_box', models.CharField(null=True, blank=True, max_length=200)),
                ('article_title1', models.CharField(null=True, blank=True, max_length=255)),
                ('article_body1', ckeditor.fields.RichTextField()),
                ('article_photo1', models.ImageField(null=True, upload_to='main_article/', blank=True)),
                ('article_title2', models.CharField(null=True, blank=True, max_length=255)),
                ('article_body2', ckeditor.fields.RichTextField()),
                ('article_photo2', models.ImageField(null=True, upload_to='main_article/', blank=True)),
                ('article_title3', models.CharField(null=True, blank=True, max_length=255)),
                ('article_body3', ckeditor.fields.RichTextField()),
                ('article_photo3', models.ImageField(null=True, upload_to='main_article/', blank=True)),
                ('created', models.DateTimeField(null=True, auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ('created',),
            },
        ),
        migrations.CreateModel(
            name='NationalInfo',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('info_title', models.CharField(blank=True, max_length=255)),
                ('info_photo', models.ImageField(upload_to='national/', blank=True)),
                ('info_body', ckeditor.fields.RichTextField()),
                ('info_author', models.CharField(blank=True, max_length=100)),
                ('info_created', models.DateTimeField(auto_now_add=True)),
                ('info_menu', models.ForeignKey(to='culture_tourism.Menu', related_name='category')),
            ],
        ),
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('news_title', models.CharField(db_index=True, blank=True, max_length=200)),
                ('news_slug', models.SlugField(blank=True, max_length=200)),
                ('news_photo', models.ImageField(upload_to='news/', blank=True)),
                ('news_body', models.TextField()),
                ('news_created', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='OtherInfo',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('address', models.CharField(blank=True, max_length=255)),
                ('phone_1', models.CharField(blank=True, max_length=17)),
                ('phone_2', models.CharField(blank=True, max_length=17)),
                ('email', models.EmailField(blank=True, max_length=254)),
                ('website', models.URLField(blank=True)),
                ('site_logo', models.ImageField(upload_to='', blank=True)),
                ('logo_footer', models.ImageField(upload_to='', blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Promo',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('promo_photo', models.ImageField(upload_to='promo/', blank=True)),
                ('promo_text', ckeditor.fields.RichTextField()),
                ('promo_created', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ('promo_created',),
            },
        ),
        migrations.CreateModel(
            name='Regions',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('region_name', models.CharField(max_length=70)),
                ('region_photo', models.ImageField(upload_to='regions/', blank=True)),
                ('region_description', ckeditor.fields.RichTextField()),
            ],
        ),
        migrations.CreateModel(
            name='RelatedToTopic',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('title', models.CharField(blank=True, max_length=100)),
                ('body', models.TextField(blank=True)),
                ('photo', models.ImageField(upload_to='related/', blank=True)),
                ('topic', models.ForeignKey(to='culture_tourism.NationalInfo', related_name='related')),
            ],
        ),
        migrations.CreateModel(
            name='Slide',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('title', models.TextField(blank=True)),
                ('photo', models.ImageField(upload_to='slide/')),
                ('description', models.TextField(blank=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='SubMenu',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('menu', models.ForeignKey(to='culture_tourism.Menu', related_name='sub_menu')),
            ],
            options={
                'ordering': ('created',),
            },
        ),
        migrations.CreateModel(
            name='Writer',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200)),
                ('photo', models.ImageField(upload_to='writers/', blank=True)),
                ('period', models.CharField(choices=[('first', 'till 12 century'), ('second', 'from 12 to 18 century'), ('third', 'from 18 century till now')], default='second', max_length=50)),
                ('description', ckeditor.fields.RichTextField()),
            ],
        ),
        migrations.AddField(
            model_name='nationalinfo',
            name='info_sub_menu',
            field=models.ForeignKey(to='culture_tourism.SubMenu', related_name='submenu'),
        ),
    ]
