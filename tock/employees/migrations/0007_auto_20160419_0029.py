# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employees', '0006_userdata_current_employee'),
    ]

    operations = [
        migrations.AddField(
            model_name='userdata',
            name='organization_1',
            field=models.CharField(default='18F', blank=True, max_length=200),
        ),
        migrations.AddField(
            model_name='userdata',
            name='organization_2',
            field=models.CharField(blank=True, max_length=200),
        ),
    ]
