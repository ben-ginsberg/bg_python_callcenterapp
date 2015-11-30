# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('callcenterapp', '0030_auto_20141116_1856'),
    ]

    operations = [
        migrations.AlterField(
            model_name='supplierbid',
            name='offer_end_date',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='supplierbid',
            name='offer_start_date',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]
