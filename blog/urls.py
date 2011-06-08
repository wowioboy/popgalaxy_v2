import tweepy
from django.conf.urls.defaults import *
from django.conf import settings
from tagging.views import tagged_object_list
from blog.models import Entry
from blog.views import *
from headlines.models import *
from shows.models import *

headlines = Headline.objects.filter(isactive=1)

shows = Show.objects.filter(isactive=1)
entries = Entry.objects.order_by('-pub_date','title').filter(status=1)
data_dict = {
	'queryset': entries,
	'date_field': 'pub_date',
    'extra_context':{'shows':shows,'headlines':headlines},
}

urlpatterns = patterns('django.views.generic.date_based',
    (r'(?P<year>\d{4})/(?P<month>[a-z]{3})/(?P<day>\w{1,2})/(?P<slug>[-\w]+)/$', 'object_detail', dict(data_dict, template_name='blog/entry.html')),
    (r'^(?P<year>\d{4})/(?P<month>[a-z]{3})/(?P<day>\w{1,2})/(?P<slug>[-\w]+)/$', 'object_detail', dict(data_dict, template_name='blog/entry.html')),
    (r'^(?P<year>\d{4})/(?P<month>[a-z]{3})/(?P<day>\w{1,2})/$','archive_day',dict(data_dict,template_name='blog/index.html')),
    (r'^(?P<year>\d{4})/(?P<month>[a-z]{3})/$','archive_month', dict(data_dict, template_name='blog/index.html')),
    (r'^(?P<year>\d{4})/$','archive_year', dict(data_dict, template_name='blog/index.html')),
    (r'^$',blog),
)





