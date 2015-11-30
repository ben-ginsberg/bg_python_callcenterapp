# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('callcenterapp', '0033_auto_20141128_2028'),
    ]

    operations = [
        migrations.AlterField(
            model_name='supplier',
            name='contact_name',
            field=models.CharField(max_length=200, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='supplier',
            name='enterprise_name',
            field=models.CharField(max_length=200, null=True, blank=True),
        ),
    ]
