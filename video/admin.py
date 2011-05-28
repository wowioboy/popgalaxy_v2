from django.contrib import admin
from video.models import *
from tinymce.widgets import TinyMCE

class RelatedBlogsInline(admin.TabularInline):
    model = RelatedBlogs
    extra = 3

class RelatedLinksInline(admin.TabularInline):
    model = RelatedLinks
    extra = 5

class VideoAdmin(admin.ModelAdmin):
    list_display = ('title', 'pub_date', 'isactive', 'featured', 'spotlight', 'incomics', 'ingames', 'inmusic', 'infilm', 'intv', 'inint', 'inextra')           
    search_fields = ['title', 'subtitle', 'details', 'tags']
    list_filter = ('pub_date', 'isactive', 'featured', 'spotlight', 'incomics', 'inmusic', 'ingames', 'infilm', 'intv', 'inint', 'inextra')
    prepopulated_fields = {"slug" : ('title',)}
    formfield_overrides = {
        WYWIWYGField: {'widget': TinyMCE(attrs={'cols': 80, 'rows': 30})}, 
    }
    fieldsets = [
        ('Section Visibility', {'fields':[('incomics','ingames','inmusic','infilm','intv','inint','inextra')],'classes':['expand']}),
        ('Basic Information', {'fields':[('isactive','featured','spotlight'),'show',('title','slug'),'subtitle','tags','details',('featuredthumb','thumbnail')]}),
        ('Details', {'fields':['carousel_text','carousel_subtext','duration','director','producer','url_home','url','pub_date','related_videos'],'classes':['collapse']}),
        ('Syndication Information', {'fields':[('wowio','wevolt','drunkduck','syndicate')],'classes':['collapse']}),
    ]
    inlines = [RelatedBlogsInline, RelatedLinksInline]

admin.site.register(Video, VideoAdmin)
