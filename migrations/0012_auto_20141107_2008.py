# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('callcenterapp', '0011_auto_20141107_1711'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='household',
            name='id',
        ),
        migrations.AlterField(
            model_name='household',
            name='cleaned_household_id',
            field=models.IntegerField(serialize=False, primary_key=True),
        ),
        migrations.AlterField(
            model_name='householdbid',
            name='date_completed',
            field=models.DateTimeField(null=True, blank=True),
        ),
    ]
