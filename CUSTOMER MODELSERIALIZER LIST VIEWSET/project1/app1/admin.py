from django.contrib import admin
from .models import Customer

# Register your models here.
class CustomerAdmin(admin.ModelAdmin):
    list_display = ['cid', 'name', 'product', 'price', 'shop', 'photo']

admin.site.register(Customer, CustomerAdmin)