from django.contrib import admin
from .models import UMKM


@admin.register(UMKM)
class UMKMAdmin(admin.ModelAdmin):
    list_display = ("id", "store_name", "beginning_capital")
    search_fields = ("id", "store_name", "beginning_capital")

    # def get_vendors_name(self, object):
    #     return object.vendors.name
