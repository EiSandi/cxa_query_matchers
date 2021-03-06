# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-05-25 07:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cxa_query', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Admission',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('description', models.CharField(max_length=200)),
                ('before_admission', models.CharField(max_length=500, null=True)),
                ('upon_admission', models.CharField(max_length=500, null=True)),
                ('after_admission', models.CharField(max_length=500, null=True)),
            ],
            options={
                'ordering': ('created',),
            },
        ),
    ]
