# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('callcenterapp', '0028_auto_20141116_1819'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cluster',
            name='id',
        ),
        migrations.AlterField(
            model_name='cluster',
            name='block_id_neighborhoods',
            field=models.ForeignKey(to='callcenterapp.Neighborhood'),
        ),
        migrations.AlterField(
            model_name='cluster',
            name='cluster_id',
            field=models.IntegerField(serialize=False, primary_key=True),
        ),
        migrations.AlterField(
            model_name='cluster',
            name='fifth_landmark_id',
            field=models.ForeignKey(related_name=b'fifth_landmark_id', blank=True, to='callcenterapp.Landmark', null=True),
        ),
        migrations.AlterField(
            model_name='cluster',
            name='fourth_landmark_id',
            field=models.ForeignKey(related_name=b'fourth_landmark_id', blank=True, to='callcenterapp.Landmark', null=True),
        ),
        migrations.AlterField(
            model_name='cluster',
            name='primary_landmark_id',
            field=models.ForeignKey(related_name=b'primary_landmark_id', blank=True, to='callcenterapp.Landmark', null=True),
        ),
        migrations.AlterField(
            model_name='cluster',
            name='second_landmark_id',
            field=models.ForeignKey(related_name=b'second_landmark_id', blank=True, to='callcenterapp.Landmark', null=True),
        ),
        migrations.AlterField(
            model_name='cluster',
            name='third_landmark_id',
            field=models.ForeignKey(related_name=b'third_landmark_id', blank=True, to='callcenterapp.Landmark', null=True),
        ),
    ]
