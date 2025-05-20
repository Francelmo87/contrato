from django.contrib import admin

from .models import Contract, ContractItem

class ContratctItemInline(admin.TabularInline):
    model = ContractItem
    extra = 1

@admin.register(Contract)
class InflowAdmin(admin.ModelAdmin):
    inlines = [ContratctItemInline]