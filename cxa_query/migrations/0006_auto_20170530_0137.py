# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-05-30 01:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cxa_query', '0005_hospital'),
    ]

    operations = [
        migrations.AlterField(
            model_name='group',
            name='area_coverage',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='group',
            name='basic_coverage',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='group',
            name='category',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='group',
            name='eligibility',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
    ]