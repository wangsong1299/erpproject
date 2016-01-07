from django.contrib import admin
from users import models


class UserAdmin(admin.ModelAdmin):
    list_display = ('nick_name', 'phone', 'role')
    search_fields = ('phone', 'nick_name')

admin.site.register(models.User, UserAdmin)