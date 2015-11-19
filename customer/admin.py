from django.contrib import admin
from customer import models

# Register your models here.
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('id', 'customers')

class SupplierAdmin(admin.ModelAdmin):
    list_display = ('id', 'suppliers')

admin.site.register(models.Customer, CustomerAdmin)
admin.site.register(models.Supplier, SupplierAdmin)
