# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-02 15:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0008_auto_20171102_1552'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='image',
            field=models.FileField(blank=True, null=True, upload_to='documents/%Y/%m/%d/'),
        ),
    ]
