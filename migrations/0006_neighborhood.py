# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('callcenterapp', '0005_household'),
    ]

    operations = [
        migrations.CreateModel(
            name='Neighborhood',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('block_id_neighborhoods', models.IntegerField()),
                ('block_id_desludgers', models.IntegerField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
