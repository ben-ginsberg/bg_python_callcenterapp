# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('callcenterapp', '0032_auto_20141123_0032'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='household',
            name='household_phone4',
        ),
        migrations.RemoveField(
            model_name='supplier',
            name='driver_name',
        ),
        migrations.RemoveField(
            model_name='supplier',
            name='driver_phone',
        ),
        migrations.RemoveField(
            model_name='supplier',
            name='hose_addition',
        ),
        migrations.RemoveField(
            model_name='supplier',
            name='license_number',
        ),
        migrations.RemoveField(
            model_name='supplier',
            name='main_garage',
        ),
        migrations.RemoveField(
            model_name='supplier',
            name='owner_name',
        ),
        migrations.RemoveField(
            model_name='supplier',
            name='owner_phone',
        ),
        migrations.RemoveField(
            model_name='supplier',
            name='plate_number',
        ),
        migrations.RemoveField(
            model_name='supplier',
            name='truck_size',
        ),
        migrations.AddField(
            model_name='supplier',
            name='contact_name',
            field=models.CharField(default='', max_length=200, blank=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='supplier',
            name='contact_phone1',
            field=models.IntegerField(null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='supplier',
            name='contact_phone2',
            field=models.IntegerField(null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='supplier',
            name='driver_firstname',
            field=models.CharField(default='', max_length=200, blank=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='supplier',
            name='driver_lastname',
            field=models.CharField(default='', max_length=200, blank=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='supplier',
            name='driver_phone1',
            field=models.IntegerField(null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='supplier',
            name='driver_phone2',
            field=models.IntegerField(null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='supplier',
            name='driver_phone3',
            field=models.IntegerField(null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='supplier',
            name='enterprise_name',
            field=models.CharField(default='', max_length=200, blank=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='supplier',
            name='owner_firstname',
            field=models.CharField(default='', max_length=200, blank=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='supplier',
            name='owner_lastname',
            field=models.CharField(default='', max_length=200, blank=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='supplier',
            name='owner_phone1',
            field=models.IntegerField(null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='supplier',
            name='owner_phone2',
            field=models.IntegerField(null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='supplier',
            name='truck1_plate',
            field=models.CharField(default='', max_length=200, blank=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='supplier',
            name='truck1_volume',
            field=models.CharField(default='', max_length=200, blank=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='supplier',
            name='truck2_plate',
            field=models.CharField(max_length=200, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='supplier',
            name='truck2_volume',
            field=models.CharField(max_length=200, null=True, blank=True),
            preserve_default=True,
        ),
    ]
