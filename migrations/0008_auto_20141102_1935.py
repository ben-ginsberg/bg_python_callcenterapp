# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('callcenterapp', '0007_auto_20141102_1905'),
    ]

    operations = [
        migrations.AddField(
            model_name='household',
            name='sixth_landmark_id',
            field=models.IntegerField(null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='household',
            name='sixth_landmark_name',
            field=models.CharField(default=' ', max_length=200, blank=True),
            preserve_default=False,
        ),
    ]
