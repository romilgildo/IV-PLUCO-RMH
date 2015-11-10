# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('plucoapp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='estudiante',
            name='id',
        ),
        migrations.RemoveField(
            model_name='profesor',
            name='id',
        ),
        migrations.AddField(
            model_name='estudiante',
            name='dni',
            field=models.CharField(default=b'12345678A', max_length=9, serialize=False, primary_key=True),
        ),
        migrations.AddField(
            model_name='profesor',
            name='dni',
            field=models.CharField(default=b'12345678A', max_length=9, serialize=False, primary_key=True),
        ),
        migrations.AlterField(
            model_name='asignatura',
            name='id',
            field=models.AutoField(serialize=False, primary_key=True),
        ),
        migrations.AlterField(
            model_name='asignatura',
            name='nombre',
            field=models.CharField(max_length=100, blank=True),
        ),
        migrations.AlterField(
            model_name='estudiante',
            name='nombre',
            field=models.CharField(max_length=100, blank=True),
        ),
        migrations.AlterField(
            model_name='profesor',
            name='nombre',
            field=models.CharField(max_length=100, blank=True),
        ),
    ]
