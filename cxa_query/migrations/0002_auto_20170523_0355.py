# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-05-23 03:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cxa_query', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='group',
            name='group_area_coverage',
            field=models.CharField(max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='group',
            name='group_basic_coverage',
            field=models.CharField(max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='group',
            name='group_eligibility',
            field=models.CharField(max_length=500, null=True),
        ),
    ]
