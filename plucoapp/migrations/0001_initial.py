# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0006_require_contenttypes_0002'),
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
                ('nick', models.ForeignKey(primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('nombre', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('tipo', models.CharField(default=b'ESTUDIANTE', max_length=10, choices=[(b'ESTUDIANTE', b'Estudiante'), (b'PROFESOR', b'Profesor')])),
            ],
        ),
    ]
