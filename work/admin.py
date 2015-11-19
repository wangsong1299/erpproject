from django.contrib import admin
from work import models

# Register your models here.
class WorkerAdmin(admin.ModelAdmin):
    list_display = ('id', 'workerID', 'worker_name')
class TrackingAdmin(admin.ModelAdmin):
    list_display = ('id', 'product_name')
    
admin.site.register(models.Worker, WorkerAdmin)
admin.site.register(models.Tracking, TrackingAdmin)