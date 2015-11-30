# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('callcenterapp', '0052_supplierbid_rejected_hh_bids'),
    ]

    operations = [
        migrations.AddField(
            model_name='householdbid',
            name='is_hh_accepted_price',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
    ]
