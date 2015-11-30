# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('callcenterapp', '0029_auto_20141116_1834'),
    ]

    operations = [
        migrations.AddField(
            model_name='household',
            name='household_phone3',
            field=models.IntegerField(null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='household',
            name='household_phone4',
            field=models.IntegerField(null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='household',
            name='household_survey_bid',
            field=models.DecimalField(null=True, max_digits=10, decimal_places=2, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='household',
            name='fifth_landmark_id',
            field=models.ForeignKey(related_name=b'household_fifth_landmark_id', blank=True, to='callcenterapp.Landmark', null=True),
        ),
        migrations.AlterField(
            model_name='household',
            name='fourth_landmark_id',
            field=models.ForeignKey(related_name=b'household_fourth_landmark_id', blank=True, to='callcenterapp.Landmark', null=True),
        ),
        migrations.AlterField(
            model_name='household',
            name='primary_landmark_id',
            field=models.ForeignKey(related_name=b'household_primary_landmark_id', blank=True, to='callcenterapp.Landmark', null=True),
        ),
        migrations.AlterField(
            model_name='household',
            name='second_landmark_id',
            field=models.ForeignKey(related_name=b'household_second_landmark_id', blank=True, to='callcenterapp.Landmark', null=True),
        ),
        migrations.AlterField(
            model_name='household',
            name='sixth_landmark_id',
            field=models.ForeignKey(related_name=b'household_sixth_landmark_id', blank=True, to='callcenterapp.Landmark', null=True),
        ),
        migrations.AlterField(
            model_name='household',
            name='third_landmark_id',
            field=models.ForeignKey(related_name=b'household_third_landmark_id', blank=True, to='callcenterapp.Landmark', null=True),
        ),
    ]
