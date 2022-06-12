from django.contrib import admin
from .models import Employee, Project

# Register your models here.
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ['eid', 'name', 'salary']

admin.site.register(Employee, EmployeeAdmin)

class ProjectAdmin(admin.ModelAdmin):
    list_display = ['name', 'employee'] 

admin.site.register(Project, ProjectAdmin)
