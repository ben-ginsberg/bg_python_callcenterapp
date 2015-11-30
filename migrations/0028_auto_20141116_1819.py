# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('callcenterapp', '0027_auto_20141116_1818'),
    ]

    operations = [
        migrations.AlterField(
            model_name='landmark',
            name='block_id_neighborhoods',
            field=models.ForeignKey(to='callcenterapp.Neighborhood'),
        ),
    ]
