# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employees', '0007_auto_20160419_0029'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='userdata',
            options={'verbose_name_plural': 'Employees', 'verbose_name': 'Employee'},
        ),
        migrations.AddField(
            model_name='userdata',
            name='billable_employee',
            field=models.BooleanField(default=True),
        ),
    ]
