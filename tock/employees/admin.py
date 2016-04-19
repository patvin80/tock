from django.contrib import admin
from django.forms.models import BaseInlineFormSet

from .models import UserData, EmployeeOrganizations

class EmployeeDataAdmin(admin.ModelAdmin):
    list_display = ('user',)

admin.site.register(UserData, EmployeeDataAdmin)
admin.site.register(EmployeeOrganizations)
