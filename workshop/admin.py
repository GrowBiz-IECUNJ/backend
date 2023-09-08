from django.contrib import admin
from .models import Workshop

@admin.register(Workshop)
class WorkshopAdmin(admin.ModelAdmin):
    list_display = ('title', 'price', 'places', 'link_meeting')
    search_fields = ('title', 'price', 'places', 'link_meeting')