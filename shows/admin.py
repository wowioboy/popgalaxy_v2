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
        (None, {'fields':['isactive',('title','slug'),'stylesheet','schedule','tags','thumbnail','body_markdown']}),
        ('Social Media', {'fields':['twitter_url','facebook_url','reddit_url','youtube_url'],'classes':['collapse']})
    ]

admin.site.register(Show, ShowsAdmin)
