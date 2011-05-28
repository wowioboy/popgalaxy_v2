from django.contrib import admin
from profiles.models import *
from tinymce.widgets import TinyMCE

class ProfileAdmin(admin.ModelAdmin):
    list_display = ('name',)           
    search_fields = ['name', 'bio_markdown']
    list_filter = ('name',)
    prepopulated_fields = {"slug" : ('name',)}
    fieldsets = (
		(None, {'fields': (('name', 'slug'), 'thumbnail', ('twitter', 'facebook_url'), 'bio_markdown', 'tags')}),
    )
    formfield_overrides = {
        WYWIWYGField: {'widget': TinyMCE(attrs={'cols': 80, 'rows': 30})}, 
    }

admin.site.register(Profile, ProfileAdmin)
