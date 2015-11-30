# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('callcenterapp', '0008_auto_20141102_1935'),
    ]

    operations = [
        migrations.AddField(
            model_name='household',
            name='household_firstname',
            field=models.CharField(default=' ', max_length=200, blank=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='household',
            name='household_is_claiming_survey',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='household',
            name='household_is_fictitious',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='household',
            name='household_is_survey',
            field=models.BooleanField(default=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='household',
            name='household_lastname',
            field=models.CharField(default=' ', max_length=200, blank=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='household',
            name='household_nickname',
            field=models.CharField(default=' ', max_length=200, blank=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='household',
            name='household_notes',
            field=models.TextField(default=' ', blank=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='household',
            name='household_num_bidders',
            field=models.IntegerField(null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='household',
            name='household_phone1',
            field=models.IntegerField(null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='household',
            name='household_phone2',
            field=models.IntegerField(null=True, blank=True),
            preserve_default=True,
        ),
    ]
