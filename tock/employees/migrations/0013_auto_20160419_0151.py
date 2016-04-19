# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('employees', '0012_auto_20160419_0146'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserData',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('start_date', models.DateField(null=True, blank=True)),
                ('end_date', models.DateField(null=True, blank=True)),
                ('current_employee', models.BooleanField(default=True)),
                ('billable_employee', models.BooleanField(default=True)),
                ('organization_1', models.CharField(max_length=200, default='18F', blank=True)),
                ('organization_2', models.CharField(max_length=200, blank=True)),
                ('organization_3', models.CharField(max_length=200, blank=True)),
                ('user', models.OneToOneField(related_name='user_data', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Employees',
                'verbose_name': 'Employee',
            },
        ),
        migrations.RemoveField(
            model_name='employees',
            name='user',
        ),
        migrations.DeleteModel(
            name='Employees',
        ),
    ]
