# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('callcenterapp', '0050_auto_20150515_0644'),
    ]

    operations = [
        migrations.RenameField(
            model_name='household',
            old_name='fixed_price_is_accepted',
            new_name='price_is_accepted',
        ),
    ]
