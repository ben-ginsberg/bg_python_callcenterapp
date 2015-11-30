# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('callcenterapp', '0031_auto_20141117_0144'),
    ]

    operations = [
        migrations.AddField(
            model_name='supplierbid',
            name='original_number_payment_advance',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='supplierbid',
            name='tank_size',
            field=models.IntegerField(default=2, blank=True, choices=[(1, b'Large'), (2, b'Small')]),
            preserve_default=True,
        ),
    ]
