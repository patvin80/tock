from django.db import models
from django.contrib.auth.models import User

class EmployeeOrganizations(models.Model):
    organization_level_1 = models.CharField(max_length=200, blank=True)
    organization_level_2 = models.CharField(max_length=200, blank=True)
    organization_level_3 = models.CharField(max_length=200, blank=True)

class UserData(models.Model):
    user = models.OneToOneField(User, related_name='user_data')
    start_date = models.DateField(blank=True, null=True)
    end_date = models.DateField(blank=True, null=True)
    current_employee = models.BooleanField(default=True)
    billable_employee = models.BooleanField(default=True)
    organization_1 = models.CharField(max_length=200, blank=True)
    organization_2 = models.CharField(max_length=200, blank=True)
    organization_3 = models.CharField(max_length=200, blank=True)

    class Meta:
        verbose_name = "Employee"
        verbose_name_plural = "Employees"
