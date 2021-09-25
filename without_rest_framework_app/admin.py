from django.contrib import admin
from without_rest_framework_app.models import Employee


class EmployeeAdmin(admin.ModelAdmin):
    list_display = ['id', 'e_no', 'e_name', 'e_salary', 'e_address']


admin.site.register(Employee, EmployeeAdmin)
