from django.contrib import admin

from .models import Bidding

@admin.register(Bidding)
class BiddingAdmin(admin.ModelAdmin):
    list_display = ('number','modality', 'year','approval_date', 'value')
    search_fields = ('number',)
