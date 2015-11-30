# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('callcenterapp', '0022_auto_20141108_1631'),
    ]

    operations = [
        migrations.AddField(
            model_name='householdbid',
            name='no_supplier_found',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
    ]
