# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('callcenterapp', '0016_remove_householdbid_cleaned_household_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='household',
            old_name='household_num_bidders',
            new_name='household_num_winners',
        ),
    ]
