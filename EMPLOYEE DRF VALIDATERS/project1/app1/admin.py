from django.contrib import admin
from .models import Employee

# Register your models here.
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ['eid', 'name', 'company', 'address', 'sal', 'email']
admin.site.register(Employee, EmployeeAdmin)
