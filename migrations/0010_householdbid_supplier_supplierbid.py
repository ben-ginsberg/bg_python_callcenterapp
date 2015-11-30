# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('callcenterapp', '0009_auto_20141102_2007'),
    ]

    operations = [
        migrations.CreateModel(
            name='HouseholdBid',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('cleaned_household_id', models.IntegerField()),
                ('bid_amount', models.DecimalField(max_digits=10, decimal_places=2)),
                ('bid_exception_1', models.BooleanField(default=False)),
                ('bid_exception_2', models.BooleanField(default=False)),
                ('bid_other_notes', models.TextField(null=True, blank=True)),
                ('bid_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('bid_win', models.BooleanField(default=False)),
                ('assigned_supplier_offer', models.IntegerField(null=True, blank=True)),
                ('household_rating_supplier', models.IntegerField(null=True, blank=True)),
                ('household_comments', models.TextField(null=True, blank=True)),
                ('job_complete', models.BooleanField()),
                ('date_completed', models.DateTimeField(blank=True)),
                ('bid_canceled', models.BooleanField()),
                ('bid_competing', models.ManyToManyField(related_name='bid_competing_rel_+', null=True, to='callcenterapp.HouseholdBid', blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Supplier',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('supplier_id', models.IntegerField(null=True, blank=True)),
                ('driver_name', models.CharField(max_length=200, blank=True)),
                ('license_number', models.CharField(max_length=200, blank=True)),
                ('plate_number', models.CharField(max_length=200, blank=True)),
                ('phone', models.IntegerField(null=True, blank=True)),
                ('owner_name', models.CharField(max_length=200, blank=True)),
                ('owner_phone', models.IntegerField(null=True, blank=True)),
                ('truck_size', models.CharField(max_length=200, blank=True)),
                ('hose_addition', models.BooleanField(default=False)),
                ('main_garage', models.CharField(max_length=200, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='SupplierBid',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('supplier_id', models.IntegerField(null=True, blank=True)),
                ('offer_start_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('offer_end_date', models.DateTimeField()),
                ('block_id_neighborhoods', models.IntegerField()),
                ('block_id_desludgers', models.IntegerField()),
                ('full_price', models.DecimalField(max_digits=10, decimal_places=2)),
                ('payment_advance', models.DecimalField(max_digits=10, decimal_places=2)),
                ('auctions_won', models.IntegerField(default=0)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
