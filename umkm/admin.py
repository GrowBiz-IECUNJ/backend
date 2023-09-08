from django.contrib import admin
from .models import UMKM

@admin.register(UMKM)
class UMKMAdmin(admin.ModelAdmin):
    list_display = ('id','owner_name', 'sex', 'store_name', 'beginning_capital', 'get_vendors_name')
    search_fields = ('id', 'owner_name', 'sex', 'store_name', 'beginning_capital')

    def get_vendors_name(self, object):
        return object.vendors.name

    