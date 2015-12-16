# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('plucoapp', '0009_auto_20151216_1721'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='nick',
            field=models.ForeignKey(default=b'1', to=settings.AUTH_USER_MODEL),
        ),
    ]
