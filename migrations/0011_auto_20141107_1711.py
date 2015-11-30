# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('callcenterapp', '0010_householdbid_supplier_supplierbid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='householdbid',
            name='bid_canceled',
            field=models.BooleanField(default=None),
        ),
        migrations.AlterField(
            model_name='householdbid',
            name='job_complete',
            field=models.BooleanField(default=None),
        ),
    ]
