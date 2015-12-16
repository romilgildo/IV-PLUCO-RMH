# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('plucoapp', '0008_usuario_nick'),
    ]

    operations = [
        migrations.AlterField(
            model_name='asignatura',
            name='nombre',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='email',
            field=models.EmailField(max_length=254, serialize=False, primary_key=True),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='nick',
            field=models.ForeignKey(default=0, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='usuario',
            name='nombre',
            field=models.CharField(max_length=100),
        ),
    ]
