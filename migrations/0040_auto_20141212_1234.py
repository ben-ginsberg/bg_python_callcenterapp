# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('callcenterapp', '0039_auto_20141212_1233'),
    ]

    operations = [
        migrations.AlterField(
            model_name='household',
            name='household_num_winners',
            field=models.IntegerField(null=True, blank=True),
        ),
    ]
