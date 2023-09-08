from django.contrib import admin
from .models import Wallet

@admin.register(Wallet)
class WalletAdmin(admin.ModelAdmin):
    list_display = ('income', 'outcome', 'type', 'description')
    search_fields = ('income', 'outcome', 'type', 'description')
