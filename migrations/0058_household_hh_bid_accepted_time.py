# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('callcenterapp', '0057_supplierbid_altenative_supplier_bids'),
    ]

    operations = [
        migrations.AddField(
            model_name='household',
            name='hh_bid_accepted_time',
            field=models.TimeField(null=True, blank=True),
            preserve_default=True,
        ),
    ]
