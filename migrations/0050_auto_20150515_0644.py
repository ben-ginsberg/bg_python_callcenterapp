# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('callcenterapp', '0049_auto_20150514_0422'),
    ]

    operations = [
        migrations.AlterField(
            model_name='household',
            name='household_category',
            field=models.IntegerField(blank=True, null=True, choices=[(1, b'Surveyed'), (2, b'Non-Surveyed'), (3, b'Fixed Price'), (4, b'Competitive')]),
        ),
    ]
