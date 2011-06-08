from django.contrib import admin
from blog.models import *
from tinymce.widgets import TinyMCE

class RelatedLinksInline(admin.TabularInline):
    model = RelatedLinks
    extra = 5

class EntryAdmin(admin.ModelAdmin):
    list_display = ('title', 'pub_date','carousel','enable_comments', 'status')           
    search_fields = ['title', 'body_markdown']
    list_filter = ('pub_date', 'enable_comments', 'status')
    prepopulated_fields = {"slug" : ('title',)}
    fieldsets = [
        ('Section Visibility', {'fields':[('incomics','ingames','inmusic','infilm','intv','inint','inextra')],'classes':['expand']}),
		('Entry Details', {'fields': (('carousel', 'enable_comments'), 'status', 'pub_date', ('title', 'slug'), 'subtitle',('author','show'), 'tags', 'source_copy', 'source', ('carousel_text', 'carousel_subtext'), ('thumbnail', 'featuredthumb'), 'body_markdown')}),
    ]
    formfield_overrides = {
        models.TextField: {'widget': TinyMCE(attrs={'cols': 100, 'rows': 40})}, 
    }
    inlines = [RelatedLinksInline]

admin.site.register(Entry, EntryAdmin)
