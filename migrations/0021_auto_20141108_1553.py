# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('callcenterapp', '0020_auto_20141108_1535'),
    ]

    operations = [
        migrations.RenameField(
            model_name='supplierbid',
            old_name='supplier_id',
            new_name='supplier',
        ),
    ]
