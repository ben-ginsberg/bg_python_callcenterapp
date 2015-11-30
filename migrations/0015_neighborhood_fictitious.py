# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('callcenterapp', '0014_auto_20141107_2044'),
    ]

    operations = [
        migrations.AddField(
            model_name='neighborhood',
            name='fictitious',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
    ]
