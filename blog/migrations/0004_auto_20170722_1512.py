# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-22 22:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_apps'),
    ]

    operations = [
        migrations.AlterField(
            model_name='apps',
            name='description',
            field=models.TextField(),
        ),
    ]