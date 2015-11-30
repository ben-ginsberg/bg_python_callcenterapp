# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('callcenterapp', '0002_cluster'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cluster',
            name='fifth_landmark_id',
            field=models.IntegerField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='cluster',
            name='fourth_landmark_id',
            field=models.IntegerField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='cluster',
            name='primary_landmark_id',
            field=models.IntegerField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='cluster',
            name='second_landmark_id',
            field=models.IntegerField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='cluster',
            name='third_landmark_id',
            field=models.IntegerField(null=True, blank=True),
        ),
    ]
