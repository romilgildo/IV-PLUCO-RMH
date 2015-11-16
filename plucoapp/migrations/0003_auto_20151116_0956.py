# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('plucoapp', '0002_auto_20151110_0837'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='asignatura',
            name='id',
        ),
        migrations.AddField(
            model_name='asignatura',
            name='nombre_id',
            field=models.CharField(default=b'nombre_id', max_length=30, serialize=False, primary_key=True),
        ),
    ]
