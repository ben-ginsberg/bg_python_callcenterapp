# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('callcenterapp', '0024_auto_20141108_1724'),
    ]

    operations = [
        migrations.AlterField(
            model_name='householdbid',
            name='household_rating_supplier',
            field=models.IntegerField(blank=True, null=True, choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)]),
        ),
    ]
