# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('callcenterapp', '0003_auto_20141101_2230'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cluster',
            name='general_comments',
            field=models.TextField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='cluster',
            name='number_additional_landmarks',
            field=models.IntegerField(null=True, blank=True),
        ),
    ]
