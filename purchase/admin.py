from django.contrib import admin
from purchase import models

# Register your models here.
class SingleAdmin(admin.ModelAdmin):
    list_display = ('id', 'productID')

class MultipleAdmin(admin.ModelAdmin):
    list_display = ('id', 'productID')

class PurchaseAdmin(admin.ModelAdmin):
    list_display = ('id', 'productID')

admin.site.register(models.Purchase_single, SingleAdmin)
admin.site.register(models.Purchase_multiple, MultipleAdmin)
admin.site.register(models.Purchase, PurchaseAdmin)