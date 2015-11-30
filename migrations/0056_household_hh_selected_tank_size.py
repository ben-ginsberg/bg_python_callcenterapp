# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('callcenterapp', '0055_household_is_hh_select_tank'),
    ]

    operations = [
        migrations.AddField(
            model_name='household',
            name='hh_selected_tank_size',
            field=models.IntegerField(null=True, blank=True),
            preserve_default=True,
        ),
    ]
