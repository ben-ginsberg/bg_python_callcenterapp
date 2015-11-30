# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('callcenterapp', '0041_auto_20141212_1247'),
    ]

    operations = [
        migrations.AlterField(
            model_name='household',
            name='cluster_id',
            field=models.IntegerField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='household',
            name='compound_number',
            field=models.IntegerField(null=True, blank=True),
        ),
    ]
