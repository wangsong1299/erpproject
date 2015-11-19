from django.contrib import admin
from storage import models

# Register your models here.
class StorageAdmin(admin.ModelAdmin):
    list_display = ('id',)
class StorageInAdmin(admin.ModelAdmin):
    list_display = ('id',)
class StorageOutAdmin(admin.ModelAdmin):
    list_display = ('id',)
class StorageMaterialAdmin(admin.ModelAdmin):
    list_display = ('id',)
   
admin.site.register(models.Storage, StorageAdmin)
   
admin.site.register(models.Storage_in, StorageInAdmin)
   
admin.site.register(models.Storage_out, StorageOutAdmin)
   
admin.site.register(models.Storage_material, StorageMaterialAdmin)