# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('callcenterapp', '0060_lowactivitydeslidger'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='LowActivityDeslidger',
            new_name='LowActivityDesludger',
        ),
    ]
