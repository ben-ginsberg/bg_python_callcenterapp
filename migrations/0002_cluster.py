# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('callcenterapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cluster',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('cluster_id', models.IntegerField()),
                ('block_id_desludgers', models.IntegerField()),
                ('block_id_neighborhoods', models.IntegerField()),
                ('sector_num_ouaga', models.IntegerField()),
                ('arrond', models.IntegerField()),
                ('neighborhood_name', models.CharField(max_length=200, blank=True)),
                ('alternate_neighborhood_name', models.CharField(max_length=200, blank=True)),
                ('closest_main_street', models.CharField(max_length=200, blank=True)),
                ('primary_landmark_name', models.CharField(max_length=200, blank=True)),
                ('primary_landmark_id', models.IntegerField(blank=True)),
                ('number_additional_landmarks', models.IntegerField(blank=True)),
                ('general_comments', models.TextField(blank=True)),
                ('second_landmark_name', models.CharField(max_length=200, blank=True)),
                ('second_landmark_id', models.IntegerField(blank=True)),
                ('third_landmark_name', models.CharField(max_length=200, blank=True)),
                ('third_landmark_id', models.IntegerField(blank=True)),
                ('fourth_landmark_name', models.CharField(max_length=200, blank=True)),
                ('fourth_landmark_id', models.IntegerField(blank=True)),
                ('fifth_landmark_name', models.CharField(max_length=200, blank=True)),
                ('fifth_landmark_id', models.IntegerField(blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
