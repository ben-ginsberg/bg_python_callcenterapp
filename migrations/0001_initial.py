# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Landmark',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('landmark_id', models.IntegerField()),
                ('cluster_id', models.IntegerField()),
                ('type_prim_sec', models.IntegerField()),
                ('block_id_desludgers', models.IntegerField()),
                ('block_id_neighborhoods', models.IntegerField()),
                ('latitude', models.FloatField()),
                ('longitude', models.FloatField()),
                ('sector_num_ouaga', models.IntegerField()),
                ('neighborhood_name', models.CharField(max_length=200)),
                ('type_of_landmark', models.IntegerField()),
                ('type_other', models.CharField(max_length=200, blank=True)),
                ('does_landmark_have_name', models.IntegerField()),
                ('landmark_name', models.CharField(max_length=200, blank=True)),
                ('closest_main_street', models.CharField(max_length=200, blank=True)),
                ('arrond', models.IntegerField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
