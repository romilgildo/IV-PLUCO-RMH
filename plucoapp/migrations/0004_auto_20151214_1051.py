# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('plucoapp', '0003_auto_20151116_0956'),
    ]

    operations = [
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('nombre', models.CharField(max_length=100, blank=True)),
                ('dni', models.CharField(default=b'12345678A', max_length=9, serialize=False, primary_key=True)),
                ('tipo', models.CharField(default=b'ESTUDIANTE', max_length=10, choices=[(b'ESTUDIANTE', b'Estudiante'), (b'PROFESOR', b'Profesor')])),
                ('nick', models.ForeignKey(blank=True, to=settings.AUTH_USER_MODEL, null=True)),
            ],
        ),
        migrations.DeleteModel(
            name='Estudiante',
        ),
        migrations.DeleteModel(
            name='Profesor',
        ),
    ]
