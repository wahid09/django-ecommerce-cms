from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import Account


# Register your models here.

class UserAdmin(BaseUserAdmin):
    list_display = ('name', 'username', 'email', 'phone_number', 'last_login', 'date_joined', 'is_active')
    list_display_links = ('name', 'username', 'email')
    readonly_fields = ('last_login', 'date_joined')
    list_filter = ('is_admin',)
    fieldsets = (
        ('Standard info', {
          'fields': ('password', 'name', 'username', 'email', 'phone_number')
      }),
      #   ('Administration', {
      #     'fields': ('is_admin', 'is_staff', 'is_superuser', 'is_active')
      # }),
        ('Permissions', {
            'fields': ('is_staff', 'is_admin', 'is_superuser', 'is_active', 'groups')
        }),
        ('Dates', {
            'fields': ('date_joined', 'last_login')
        }),
    )
    search_fields = ('email', 'name', 'username')
    ordering = ('email', 'name', 'username', 'last_login')
    filter_horizontal = ()


admin.site.register(Account, UserAdmin)
