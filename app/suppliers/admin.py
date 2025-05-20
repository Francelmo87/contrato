from django.contrib import admin

from .models import Supplier

@admin.register(Supplier)
class SupplierAdmin(admin.ModelAdmin):
    list_display = ('name','cnpj', 'representative','rg', 'cpf')
    search_fields = ('name',)