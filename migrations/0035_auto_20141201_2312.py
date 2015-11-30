# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('callcenterapp', '0034_auto_20141128_2030'),
    ]

    operations = [
        migrations.AddField(
            model_name='payment',
            name='date_payment_sent',
            field=models.DateTimeField(null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='payment',
            name='payment_sent',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='payment',
            name='user_job_done',
            field=models.ForeignKey(related_name=b'user_job_done', to=settings.AUTH_USER_MODEL, null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='payment',
            name='user_payment_confirmed',
            field=models.ForeignKey(related_name=b'user_payment_confirmed', to=settings.AUTH_USER_MODEL, null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='payment',
            name='user_payment_sent',
            field=models.ForeignKey(related_name=b'user_payment_sent', to=settings.AUTH_USER_MODEL, null=True),
            preserve_default=True,
        ),
    ]
