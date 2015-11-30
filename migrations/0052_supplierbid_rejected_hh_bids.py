# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('callcenterapp', '0051_auto_20150518_0504'),
    ]

    operations = [
        migrations.AddField(
            model_name='supplierbid',
            name='rejected_hh_bids',
            field=models.ManyToManyField(default=None, to='callcenterapp.HouseholdBid', null=True),
            preserve_default=True,
        ),
    ]
