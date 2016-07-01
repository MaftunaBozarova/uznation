# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('culture_tourism', '0006_auto_20160623_1604'),
    ]

    operations = [
        migrations.AlterField(
            model_name='generalinfo',
            name='info_sub_menu',
            field=models.ForeignKey(to='culture_tourism.SubMenu', related_name='submenu', null=True, blank=True),
        ),
    ]
