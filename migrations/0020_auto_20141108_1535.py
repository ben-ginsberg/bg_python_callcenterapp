# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('callcenterapp', '0019_auto_20141108_1523'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='supplierbid',
            name='block_id_desludgers',
        ),
        migrations.RemoveField(
            model_name='supplierbid',
            name='block_id_neighborhoods',
        ),
        migrations.AddField(
            model_name='supplierbid',
            name='neighborhoods_serviced',
            field=models.ManyToManyField(to='callcenterapp.Neighborhood', null=True, blank=True),
            preserve_default=True,
        ),
    ]
