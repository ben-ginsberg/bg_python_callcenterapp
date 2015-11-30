# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('callcenterapp', '0058_household_hh_bid_accepted_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='household',
            name='hh_bid_accepted_time',
            field=models.DateTimeField(null=True, blank=True),
        ),
    ]
