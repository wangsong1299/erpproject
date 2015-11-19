from django.contrib import admin
from finance import models

# Register your models here.
class FinanceAdmin(admin.ModelAdmin):
    list_display = ('id', 'product_name')

admin.site.register(models.Finance, FinanceAdmin)


