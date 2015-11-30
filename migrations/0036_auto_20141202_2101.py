# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('callcenterapp', '0035_auto_20141201_2312'),
    ]

    operations = [
        migrations.AlterField(
            model_name='household',
            name='household_notes',
            field=models.TextField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='household',
            name='latitude',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='household',
            name='longitude',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='supplierbid',
            name='tank_size',
            field=models.IntegerField(default=2, blank=True, choices=[(1, b'Grand'), (2, b'Petit')]),
        ),
    ]
