# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-11 15:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newsroom', '0058_auto_20171010_1213'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='external_primary_image',
            field=models.CharField(blank=True, help_text='Use this instead of primary. But note that if primary image has a value, it overrides this.', max_length=500, verbose_name='alternative URL'),
        ),
    ]
