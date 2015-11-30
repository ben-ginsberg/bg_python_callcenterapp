# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('callcenterapp', '0053_householdbid_is_hh_accepted_price'),
    ]

    operations = [
        migrations.RenameField(
            model_name='householdbid',
            old_name='is_hh_accepted_price',
            new_name='is_hh_refuse_price',
        ),
    ]
