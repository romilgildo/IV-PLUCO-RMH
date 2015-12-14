# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('plucoapp', '0004_auto_20151214_1051'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usuario',
            name='nick',
        ),
    ]
