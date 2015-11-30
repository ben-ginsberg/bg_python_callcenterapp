# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('callcenterapp', '0054_auto_20150522_0606'),
    ]

    operations = [
        migrations.AddField(
            model_name='household',
            name='is_hh_select_tank',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
    ]
