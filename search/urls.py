from django.conf.urls.defaults import *
from search.views import *

urlpatterns = patterns('',
    (r'^$', results),
)
