# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employees', '0010_auto_20160419_0131'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employees',
            name='organization_1',
            field=models.CharField(blank=True, max_length=200),
        ),
    ]
