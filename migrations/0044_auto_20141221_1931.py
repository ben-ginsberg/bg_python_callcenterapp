# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('callcenterapp', '0043_auto_20141221_1931'),
    ]

    operations = [
        migrations.AlterField(
            model_name='supplier',
            name='supplier_id',
            field=models.IntegerField(serialize=False, primary_key=True),
        ),
    ]
