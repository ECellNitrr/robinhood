from django.contrib import admin
from .models import Item, Donation
# Register your models here.

class ItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'status', 'description')
    search_fields = ('name', 'status')
    list_filter = ('status',)
    ordering = ('-created_at',)
    readonly_fields = ('created_at', 'modified_at')

class DonationAdmin(admin.ModelAdmin):
    list_display = ('profile', 'item', 'quantity', 'status', 'description')
    search_fields = ('profile', 'item')
    list_filter = ('profile', 'item', 'item_condition')
    ordering = ('-created_at',)
    readonly_fields = ('created_at', 'modified_at')

admin.site.register(Item, ItemAdmin)
admin.site.register(Donation, DonationAdmin)