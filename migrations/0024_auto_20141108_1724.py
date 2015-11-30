# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('callcenterapp', '0023_householdbid_no_supplier_found'),
    ]

    operations = [
        migrations.RenameField(
            model_name='supplier',
            old_name='phone',
            new_name='driver_phone',
        ),
    ]
