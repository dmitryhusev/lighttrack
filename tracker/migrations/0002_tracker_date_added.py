# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-14 13:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tracker', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='tracker',
            name='date_added',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
