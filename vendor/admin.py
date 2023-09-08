from django.contrib import admin
from .models import Vendor

@admin.register(Vendor)
class VendorAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone_number', 'get_product_name')
    search_fields = ('name', 'phone_number')

    def get_product_name(self, object):
        return object.product_name.name