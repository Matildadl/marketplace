from django.contrib import admin

from .models import Category, Item

class ItemAdmin(admin.ModelAdmin):
    list_display = ['name', 'description', 'price', 'is_sold', 'created_by', 'created_at', 'category']
    list_filter = ['is_sold', 'created_at', 'category']
    search_fields = ['name', 'description']
    
admin.site.register(Category)
admin.site.register(Item)
