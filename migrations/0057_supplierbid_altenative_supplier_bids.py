# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('callcenterapp', '0056_household_hh_selected_tank_size'),
    ]

    operations = [
        migrations.AddField(
            model_name='supplierbid',
            name='altenative_supplier_bids',
            field=models.ManyToManyField(default=None, related_name=b'alternative_supplierbids', null=True, to='callcenterapp.HouseholdBid'),
            preserve_default=True,
        ),
    ]
