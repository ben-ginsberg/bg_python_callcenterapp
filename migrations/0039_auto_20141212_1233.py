# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('callcenterapp', '0038_auto_20141211_1553'),
    ]

    operations = [
        migrations.AlterField(
            model_name='household',
            name='household_num_winners',
            field=models.IntegerField(),
        ),
    ]
