# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-10-05 06:26
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('instagramapp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='image',
            name='profile',
        ),
    ]
