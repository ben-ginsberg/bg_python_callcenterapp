# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('callcenterapp', '0065_supplier_household_set_number'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='supplier',
            name='household_set_number',
        ),
        migrations.AddField(
            model_name='supplierbid',
            name='household_set_number',
            field=models.IntegerField(blank=True, null=True, choices=[(1, b'Surveyed'), (2, b'Non-Surveyed'), (3, b'Fixed Price'), (4, b'Competitive')]),
            preserve_default=True,
        ),
    ]
