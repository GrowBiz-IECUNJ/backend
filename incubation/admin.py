from django.contrib import admin
from .models import Incubation, Investor, Portfolio


@admin.register(Incubation)
class IncubationAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "business_category", "get_investor_name")
    search_fields = ("id", "name", "business_category")

    def get_investor_name(self, object):
        return object.investor.name


@admin.register(Investor)
class InvestorAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "description")
    search_fields = ("id", "name", "description")


@admin.register(Portfolio)
class PortfolioAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "description")
    search_fields = ("id", "title", "description")
