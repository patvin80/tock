# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employees', '0011_auto_20160419_0145'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employees',
            name='organization_1',
            field=models.CharField(default='18F', max_length=200, blank=True),
        ),
    ]
