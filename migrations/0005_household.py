# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('callcenterapp', '0004_auto_20141101_2231'),
    ]

    operations = [
        migrations.CreateModel(
            name='Household',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('cleaned_household_id', models.IntegerField()),
                ('cluster_id', models.IntegerField()),
                ('compound_number', models.IntegerField()),
                ('block_id_desludgers', models.IntegerField()),
                ('block_id_neighborhoods', models.IntegerField()),
                ('sector_num_ouaga', models.IntegerField()),
                ('arrond', models.IntegerField()),
                ('neighborhood_name', models.CharField(max_length=200, blank=True)),
                ('alternate_neighborhood_name', models.CharField(max_length=200, blank=True)),
                ('latitude', models.FloatField()),
                ('longitude', models.FloatField()),
                ('closest_main_street', models.CharField(max_length=200, blank=True)),
                ('primary_landmark_name', models.CharField(max_length=200, blank=True)),
                ('primary_landmark_id', models.IntegerField(null=True, blank=True)),
                ('number_additional_landmarks', models.IntegerField(null=True, blank=True)),
                ('second_landmark_id', models.IntegerField(null=True, blank=True)),
                ('second_landmark_name', models.CharField(max_length=200, blank=True)),
                ('third_landmark_id', models.IntegerField(null=True, blank=True)),
                ('third_landmark_name', models.CharField(max_length=200, blank=True)),
                ('fourth_landmark_id', models.IntegerField(null=True, blank=True)),
                ('fourth_landmark_name', models.CharField(max_length=200, blank=True)),
                ('fifth_landmark_id', models.IntegerField(null=True, blank=True)),
                ('fifth_landmark_name', models.CharField(max_length=200, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
