# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employees', '0008_auto_20160419_0121'),
    ]

    operations = [
        migrations.AddField(
            model_name='userdata',
            name='organization_3',
            field=models.CharField(max_length=200, blank=True),
        ),
    ]
