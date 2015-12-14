# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('plucoapp', '0005_remove_usuario_nick'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usuario',
            name='dni',
        ),
        migrations.AddField(
            model_name='usuario',
            name='email',
            field=models.EmailField(max_length=254, unique=True, serialize=False, primary_key=True, blank=True),
        ),
        migrations.AddField(
            model_name='usuario',
            name='nick',
            field=models.ForeignKey(blank=True, to=settings.AUTH_USER_MODEL, null=True),
        ),
    ]
