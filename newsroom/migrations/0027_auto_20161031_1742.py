# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-10-31 15:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newsroom', '0026_auto_20161031_1741'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='id_or_db',
            field=models.CharField(blank=True, max_length=20, verbose_name='ID or date of birth'),
        ),
    ]
