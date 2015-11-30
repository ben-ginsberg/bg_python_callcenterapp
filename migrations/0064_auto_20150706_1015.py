# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('callcenterapp', '0063_supplierbid_supplier_rank'),
    ]

    operations = [
        migrations.AlterField(
            model_name='supplierbid',
            name='supplier_rank',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
