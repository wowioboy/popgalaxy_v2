from django.contrib import admin
from shows.models import *
from tinymce.widgets import TinyMCE

class ShowsAdmin(admin.ModelAdmin):
    list_display = ('title',)
    search_fields = ['title', 'body_markdown']
    list_filter = ('title',)
    prepopulated_fields = {"slug" : ('title',)}
    formfield_overrides = {
        WYWIWYGField: {'widget': TinyMCE(attrs={'cols': 80, 'rows': 30})}, 
    }
    fieldsets = [
        (None, {'fields':['isactive',('title','slug'),'thumbnail','body_markdown','tags']}),
    ]

admin.site.register(Show, ShowsAdmin)
