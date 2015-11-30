# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('callcenterapp', '0048_auto_20141229_0452'),
    ]

    operations = [
        migrations.AddField(
            model_name='household',
            name='fixed_price_is_accepted',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='household',
            name='household_category',
            field=models.IntegerField(default=1, blank=True, choices=[(1, b'Surveyed'), (2, b'Non-Surveyed'), (3, b'Fixed Price'), (4, b'Competitive')]),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='household',
            name='household_fixed_price',
            field=models.DecimalField(null=True, max_digits=10, decimal_places=2, blank=True),
            preserve_default=True,
        ),
    ]
