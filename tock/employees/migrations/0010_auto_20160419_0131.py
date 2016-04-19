# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('employees', '0009_userdata_organization_3'),
    ]

    operations = [
        migrations.CreateModel(
            name='EmployeeOrganizations',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('organization_level_1', models.CharField(blank=True, max_length=200)),
                ('organization_level_2', models.CharField(blank=True, max_length=200)),
                ('organization_level_3', models.CharField(blank=True, max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Employees',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('start_date', models.DateField(null=True, blank=True)),
                ('end_date', models.DateField(null=True, blank=True)),
                ('current_employee', models.BooleanField(default=True)),
                ('billable_employee', models.BooleanField(default=True)),
                ('organization_2', models.CharField(blank=True, max_length=200)),
                ('organization_3', models.CharField(blank=True, max_length=200)),
                ('organization_1', models.ForeignKey(to='employees.EmployeeOrganizations', verbose_name='Employee Organizations', default='18F')),
                ('user', models.OneToOneField(related_name='user_data', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Employee',
                'verbose_name_plural': 'Employees',
            },
        ),
        migrations.RemoveField(
            model_name='userdata',
            name='user',
        ),
        migrations.DeleteModel(
            name='UserData',
        ),
    ]
