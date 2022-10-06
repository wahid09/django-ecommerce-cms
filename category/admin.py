from django.contrib import admin
from .models import Category, CategorySection, SubCategory

# Register your models here.


class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
    list_display = ('name', 'is_active', 'created_at')
    list_editable = ('is_active',)
    search_fields = ('name', 'slug')


admin.site.register(Category, CategoryAdmin)


admin.site.register(CategorySection)

admin.site.register(SubCategory)


