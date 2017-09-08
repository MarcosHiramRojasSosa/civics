# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-09-08 10:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('models', '0025_auto_20170907_0842'),
    ]

    operations = [
        migrations.AddField(
            model_name='city',
            name='event_related',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='city',
            name='initiative_related',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='event',
            name='date',
            field=models.DateField(help_text='Indica qué día se celebra o empieza el evento', verbose_name='Fecha del evento'),
        ),
        migrations.AlterField(
            model_name='event',
            name='expiration',
            field=models.DateField(blank=True, help_text='Indica opcionalmente en eventos de varios dias la fecha en que acaba el evento.', null=True, verbose_name='Fecha de fin'),
        ),
        migrations.AlterField(
            model_name='event',
            name='periodicity',
            field=models.CharField(blank=True, help_text='Especifica, en ese caso, la periodicidad del evento. Puedes indicar la fecha de fin en el siguiente campo', max_length=200, null=True, verbose_name='Periodicidad'),
        ),
    ]
