from django.contrib import admin

from .models import ListItem

@admin.register(ListItem)
class ListItemAdmin(admin.ModelAdmin):
    list_display = ('content',)
    search_fields = ('content',)
