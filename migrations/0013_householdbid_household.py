# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('callcenterapp', '0012_auto_20141107_2008'),
    ]

    operations = [
        migrations.AddField(
            model_name='householdbid',
            name='household',
            field=models.ForeignKey(default=33, to='callcenterapp.Household'),
            preserve_default=False,
        ),
    ]
