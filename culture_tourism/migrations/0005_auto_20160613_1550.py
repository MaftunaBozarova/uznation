# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('culture_tourism', '0004_auto_20160613_1351'),
    ]

    operations = [
        migrations.AddField(
            model_name='otherinfo',
            name='logo_footer',
            field=models.ImageField(blank=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='otherinfo',
            name='site_logo',
            field=models.ImageField(blank=True, upload_to=''),
        ),
    ]
