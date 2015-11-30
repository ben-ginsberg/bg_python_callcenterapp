# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('callcenterapp', '0047_auto_20141221_1943'),
    ]

    operations = [
        migrations.AddField(
            model_name='supplierbid',
            name='neighborhoods_serviced_2',
            field=models.ForeignKey(related_name=b'neighborhoods_serviced_2', blank=True, to='callcenterapp.Neighborhood', null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='supplierbid',
            name='payment_advance',
            field=models.DecimalField(default=0.0, max_digits=10, decimal_places=2),
        ),
        migrations.AlterField(
            model_name='supplierbid',
            name='tank_size',
            field=models.IntegerField(default=1, blank=True, choices=[(1, b'Petit'), (2, b'Grand')]),
        ),
    ]
