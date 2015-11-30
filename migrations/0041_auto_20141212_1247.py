# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('callcenterapp', '0040_auto_20141212_1234'),
    ]

    operations = [
        migrations.AlterField(
            model_name='household',
            name='household_num_winners',
            field=models.IntegerField(),
        ),
    ]
