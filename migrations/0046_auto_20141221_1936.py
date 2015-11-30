# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('callcenterapp', '0045_auto_20141221_1932'),
    ]

    operations = [
        migrations.AlterField(
            model_name='supplier',
            name='owner_phone2',
            field=models.CharField(max_length=100, null=True, blank=True),
        ),
    ]
