from django.contrib import admin
from assetlocker.models import *

class AssetAdmin(admin.ModelAdmin):
    list_display = ('title', 'asset_date', 'get_absolute_url')
    search_fields = ['title',]

admin.site.register(Asset, AssetAdmin)
