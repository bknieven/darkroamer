# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2018-01-13 17:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_note'),
    ]

    operations = [
        migrations.AddField(
            model_name='note',
            name='note_email',
            field=models.TextField(default=''),
        ),
    ]
