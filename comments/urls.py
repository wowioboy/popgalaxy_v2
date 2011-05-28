from django.conf.urls.defaults import *
from comments.views import *

urlpatterns = patterns('', 
    (r'^add/(?P<object_type>.*)/(?P<id>.*)/$', add_comment),
    (r'^(?P<object_type>.*)/(?P<id>.*)/$', get_comments),
)
