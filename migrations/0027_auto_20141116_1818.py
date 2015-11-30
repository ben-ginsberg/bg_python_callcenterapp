# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('callcenterapp', '0026_payment'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='landmark',
            name='id',
        ),
        migrations.AlterField(
            model_name='landmark',
            name='landmark_id',
            field=models.IntegerField(serialize=False, primary_key=True),
        ),
    ]
