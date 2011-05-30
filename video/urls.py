from django.conf.urls.defaults import *
from video.views import *

urlpatterns = patterns('',
    (r'^(?P<slug>[a-zA-Z0-9_.-]+)/$',video_detail),
    (r'^$',video_list),
)

