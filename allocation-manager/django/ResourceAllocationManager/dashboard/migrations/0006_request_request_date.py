# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-12-01 07:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0005_remove_request_request_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='request',
            name='request_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
