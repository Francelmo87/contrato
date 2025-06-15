from django.contrib import admin

from .models import Contract, ItemContract, Amendment, ItemAmendment

class ContratctItemInline(admin.TabularInline):
    model = ItemContract
    extra = 1

@admin.register(Contract)
class ContractAdmin(admin.ModelAdmin):
    inlines = [ContratctItemInline]

class AmendmentItemInline(admin.TabularInline):
    model = ItemAmendment
    extra = 1

@admin.register(Amendment)
class AmendmentAdmin(admin.ModelAdmin):
    inlines = [AmendmentItemInline]
