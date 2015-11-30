# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('callcenterapp', '0018_householdbid_bid_win_pay'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='supplier',
            name='id',
        ),
        migrations.AddField(
            model_name='supplierbid',
            name='number_payment_advance',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='supplier',
            name='supplier_id',
            field=models.IntegerField(serialize=False, primary_key=True),
        ),
        migrations.AlterField(
            model_name='supplierbid',
            name='supplier_id',
            field=models.ForeignKey(to='callcenterapp.Supplier'),
        ),
    ]
