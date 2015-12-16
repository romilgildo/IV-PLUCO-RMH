# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    replaces = [(b'plucoapp', '0001_initial'), (b'plucoapp', '0002_auto_20151110_0837'), (b'plucoapp', '0003_auto_20151116_0956'), (b'plucoapp', '0004_auto_20151214_1051'), (b'plucoapp', '0005_remove_usuario_nick'), (b'plucoapp', '0006_auto_20151214_1142'), (b'plucoapp', '0007_remove_usuario_nick')]

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Asignatura',
            fields=[
                ('nombre', models.CharField(max_length=100, blank=True)),
                ('nombre_id', models.CharField(default=b'nombre_id', max_length=30, serialize=False, primary_key=True)),
            ],
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('nombre', models.CharField(max_length=100, blank=True)),
                ('tipo', models.CharField(default=b'ESTUDIANTE', max_length=10, choices=[(b'ESTUDIANTE', b'Estudiante'), (b'PROFESOR', b'Profesor')])),
                ('email', models.EmailField(max_length=254, unique=True, serialize=False, primary_key=True, blank=True)),
            ],
        ),
    ]
