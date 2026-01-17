from django.contrib import admin
from ..models import Menu, Page


@admin.register(Menu)
class MenuAdmin(admin.ModelAdmin):
    list_display = ('name_display', 'slug', 'level', 'order', 'is_active')
    list_filter = ('level', 'is_active', 'parent')
    search_fields = ('name', 'slug')
    ordering = ('level', 'order', 'name')
    prepopulated_fields = {'slug': ('name',)}

    def name_display(self, obj):
        return f"{'—' * obj.level} {obj.name}"

    name_display.short_description = 'Name'


@admin.register(Page)
class PageAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'menu', 'created_at')
    list_filter = ('menu', 'created_at')
    search_fields = ('title', 'slug', 'content')
    prepopulated_fields = {'slug': ('title',)}

