# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2016-09-29 06:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('learndb', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='high',
            field=models.IntegerField(default=10),
            preserve_default=False,
        ),
    ]
