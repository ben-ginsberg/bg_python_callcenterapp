# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('callcenterapp', '0062_supplierbid_random_supplier_bid'),
    ]

    operations = [
        migrations.AddField(
            model_name='supplierbid',
            name='supplier_rank',
            field=models.PositiveIntegerField(null=True),
            preserve_default=True,
        ),
    ]
