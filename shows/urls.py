import tweepy
from django.conf.urls.defaults import *
from django.conf import settings
from tagging.views import tagged_object_list
from shows.models import Show
from shows.views import *
from headlines.models import *

urlpatterns = patterns('',
    (r'^(?P<slug>.*)/$', show_page),
)