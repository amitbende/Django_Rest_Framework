from django.contrib import admin
from .models import Employee

# Register your models here.
class EmpoloyeeAdmin(admin.ModelAdmin):
    list_display = ['eid', 'name', 'company', 'department', 'salary', 'address', 'picture']

admin.site.register(Employee, EmpoloyeeAdmin)
