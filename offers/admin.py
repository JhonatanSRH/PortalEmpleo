"""Offers admin."""

# Django
from django.contrib import admin

# Models
from offers.models import Offer, OfferApplication


class OfferModelAdmin(admin.ModelAdmin):
    """Offer model admin."""
    fiels = ('title', 'description', 'salary', 'is_active', 'creator_id', 'updater_id',)
    list_display = ('title', 'description', 'salary', 'is_active', 'creator_id', 'updater_id', 'created', 'modified',)
    list_filter = ('created', 'modified')

class OfferApplicationModelAdmin(admin.ModelAdmin):
    """Offer application model admin."""
    fiels = ('applied_id', 'offer',)
    list_display = ('applied_id', 'offer', 'created', 'modified',)
    list_filter = ('created', 'modified')

admin.site.register(Offer, OfferModelAdmin)
admin.site.register(OfferApplication, OfferApplicationModelAdmin)