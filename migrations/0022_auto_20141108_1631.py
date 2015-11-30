# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('callcenterapp', '0021_auto_20141108_1553'),
    ]

    operations = [
        migrations.AlterField(
            model_name='householdbid',
            name='assigned_supplier_offer',
            field=models.ForeignKey(blank=True, to='callcenterapp.SupplierBid', null=True),
        ),
    ]
