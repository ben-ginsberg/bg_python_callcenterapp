# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('callcenterapp', '0036_auto_20141202_2101'),
    ]

    operations = [
        migrations.AlterField(
            model_name='household',
            name='latitude',
            field=models.FloatField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='household',
            name='longitude',
            field=models.FloatField(null=True, blank=True),
        ),
    ]
