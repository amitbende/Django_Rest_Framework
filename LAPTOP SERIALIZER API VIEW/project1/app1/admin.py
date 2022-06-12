from pyclbr import Class
from django.contrib import admin
from .models import Laptop

# Register your models here.
class LaptopAdmin(admin.ModelAdmin):
    list_display = ['laptop_id', 'name', 'brand', 'model', 'price', 'processer']
admin.site.register(Laptop, LaptopAdmin)
