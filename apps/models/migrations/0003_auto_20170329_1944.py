# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-29 19:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('models', '0002_auto_20170329_1940'),
    ]

    operations = [
        migrations.AlterField(
            model_name='initiative',
            name='agent',
            field=models.CharField(choices=[('IM', 'Iniciativas municipales / Gobierno'), ('IC', 'Iniciativa ciudadana'), ('OI', 'Organismos internacionales'), ('ES', 'Empresa social / Startup'), ('UO', 'Universidades / ONG'), ('JA', 'Juntas / Asociaciones de vecinos'), ('CC', 'Conquistas ciudadanas del pasado')], default='IM', help_text='El tipo de agente involucrado en la iniciativa', max_length=2, verbose_name='tipo de agente'),
        ),
        migrations.AlterField(
            model_name='initiative',
            name='space',
            field=models.CharField(choices=[('CC', 'Centro cultural/comunitario'), ('EI', 'Efímero e itinerante'), ('IT', 'Intercambio / Trueque'), ('DI', 'Digital'), ('EA', 'Encuentros / Acciones'), ('EP', 'Escuelas populares'), ('HU', 'Huerto urbano/rural'), ('IU', 'Intervenciones urbanas'), ('MC', 'Medios comunitarios de comunicación'), ('MS', 'Mercado social / Comercios'), ('SE', 'Solares / Espacios recuperados'), ('EM', 'Espacios colaborativos/maker'), ('OT', 'Otro')], default='CC', help_text='El tipo de espacio asociado a la iniciativa', max_length=2, verbose_name='Tipo de espacio'),
        ),
        migrations.AlterField(
            model_name='initiative',
            name='topic',
            field=models.CharField(choices=[('DC', 'Desarrollo comunitario'), ('AU', 'Arte urbano'), ('CL', 'Cultura libre'), ('DS', 'Deporte / Salud / Cuidados'), ('ID', 'Igualdad / Derechos / Memoria'), ('EC', 'Ecología / Consumo'), ('OE', 'Otras economías'), ('EE', 'Educación expandida'), ('CT', 'Ciencia / Tecnología'), ('MS', 'Movilidad sostenible'), ('PG', 'Política y gobernanza'), ('UP', 'Urbanismo / Patrimonio'), ('OT', 'Otro')], default='DC', help_text='El tema de la iniciativa', max_length=2, verbose_name='Tema'),
        ),
    ]