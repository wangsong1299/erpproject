from django.contrib import admin
from sales import models

# Register your models here.
class QuotationAdmin(admin.ModelAdmin):
    list_display = ('id', 'product_name')

class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'productID')

class ProcessAdmin(admin.ModelAdmin):
    list_display = ('id', 'productID')

class DeliveryAdmin(admin.ModelAdmin):
    list_display = ('id', 'productID')

class CostAdmin(admin.ModelAdmin):
    list_display = ('id', 'productID')

class ImageAdmin(admin.ModelAdmin):
    list_display = ('id', 'productID')

admin.site.register(models.Quotation, QuotationAdmin)
admin.site.register(models.Order, OrderAdmin)
admin.site.register(models.Process, ProcessAdmin)
admin.site.register(models.Delivery, DeliveryAdmin)
admin.site.register(models.Cost, CostAdmin)
admin.site.register(models.Image, ImageAdmin)
