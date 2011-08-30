from django.contrib import admin
from tinymce.widgets import TinyMCE
from corp.models import *

class CorporateAdmin(admin.ModelAdmin):
    list_display = ('section',)           
    #search_fields = ['section',]
    list_filter = ('section',)
    formfield_overrides = {
        models.TextField: {'widget': TinyMCE(attrs={'cols': 100, 'rows': 40})},
    }

admin.site.register(Corporate, CorporateAdmin)