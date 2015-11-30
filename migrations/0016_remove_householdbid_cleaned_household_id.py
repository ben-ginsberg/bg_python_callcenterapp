# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('callcenterapp', '0015_neighborhood_fictitious'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='householdbid',
            name='cleaned_household_id',
        ),
    ]
