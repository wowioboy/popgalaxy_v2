from django.contrib import admin
from headlines.models import *

class HeadlineAdmin(admin.ModelAdmin):
    list_display = ('title','isactive',)           
    search_fields = ['title']
    fieldsets = [
        ('Sections Visibility Info.', {'fields':[('incomics','ingames','inmusic','infilm','intv','inint','inextra')],'classes':['expand']}),
        (None, {'fields':['isactive','title']}),
    ]

admin.site.register(Headline, HeadlineAdmin)