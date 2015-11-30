# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('callcenterapp', '0013_householdbid_household'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='neighborhood',
            name='id',
        ),
        migrations.AddField(
            model_name='neighborhood',
            name='related_neighborhoods',
            field=models.ManyToManyField(related_name='related_neighborhoods_rel_+', null=True, to='callcenterapp.Neighborhood', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='household',
            name='block_id_neighborhoods',
            field=models.ForeignKey(to='callcenterapp.Neighborhood'),
        ),
        migrations.AlterField(
            model_name='neighborhood',
            name='block_id_neighborhoods',
            field=models.IntegerField(serialize=False, primary_key=True),
        ),
    ]
