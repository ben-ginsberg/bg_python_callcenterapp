# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('callcenterapp', '0025_auto_20141108_1950'),
    ]

    operations = [
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('advance_used', models.BooleanField(default=False)),
                ('amount_due', models.DecimalField(max_digits=10, decimal_places=2)),
                ('date_opened', models.DateTimeField(default=django.utils.timezone.now)),
                ('date_closed', models.DateTimeField(null=True, blank=True)),
                ('payment_completed', models.BooleanField(default=False)),
                ('householdbid', models.ForeignKey(to='callcenterapp.HouseholdBid')),
                ('supplierbid', models.ForeignKey(to='callcenterapp.SupplierBid')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
