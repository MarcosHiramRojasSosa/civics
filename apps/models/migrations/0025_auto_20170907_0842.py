# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-09-07 08:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('models', '0024_auto_20170815_1801'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='expiration',
            field=models.DateField(blank=True, help_text='Indica opcionalmente en eventos de varios dias la fecha en que acaba el evento.', null=True, verbose_name='Periodicidad'),
        ),
        migrations.AlterField(
            model_name='event',
            name='periodicity',
            field=models.CharField(blank=True, help_text='Especifica, en ese caso, la periodicidad del evento.', max_length=200, null=True, verbose_name='Periodicidad'),
        ),
    ]
