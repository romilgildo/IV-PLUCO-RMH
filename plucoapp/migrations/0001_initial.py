# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Asignatura',
            fields=[
                ('nombre', models.CharField(max_length=100)),
                ('nombre_id', models.CharField(default=b'nombre_id', max_length=30, serialize=False, primary_key=True)),
            ],
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('nombre', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254, serialize=False, primary_key=True)),
                ('tipo', models.CharField(default=b'ESTUDIANTE', max_length=10, choices=[(b'ESTUDIANTE', b'Estudiante'), (b'PROFESOR', b'Profesor')])),
                ('nick', models.ForeignKey(to=settings.AUTH_USER_MODEL, null=True)),
            ],
        ),
    ]
