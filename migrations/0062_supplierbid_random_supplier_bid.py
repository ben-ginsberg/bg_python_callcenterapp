# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('callcenterapp', '0061_auto_20150606_0751'),
    ]

    operations = [
        migrations.AddField(
            model_name='supplierbid',
            name='random_supplier_bid',
            field=models.ManyToManyField(default=None, related_name=b'random_supplierbid', null=True, to='callcenterapp.HouseholdBid'),
            preserve_default=True,
        ),
    ]
