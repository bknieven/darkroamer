# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2018-01-15 16:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_note_note_email'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='article',
            options={'ordering': ['-pub_date'], 'verbose_name': 'Blog Article', 'verbose_name_plural': 'Blog Articles'},
        ),
        migrations.RemoveField(
            model_name='article',
            name='title_word',
        ),
        migrations.AddField(
            model_name='article',
            name='is_publish',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='article',
            name='mod_date',
            field=models.DateTimeField(auto_now=True, verbose_name='article modified'),
        ),
        migrations.AddField(
            model_name='article',
            name='slug',
            field=models.SlugField(default='', max_length=200),
        ),
    ]
