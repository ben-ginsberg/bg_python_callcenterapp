# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('callcenterapp', '0006_neighborhood'),
    ]

    operations = [
        migrations.AlterField(
            model_name='landmark',
            name='does_landmark_have_name',
            field=models.IntegerField(null=True),
        ),
    ]
