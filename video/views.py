from django.template import RequestContext
from django.shortcuts import render_to_response
from video.models import *
from headlines.models import *


def video_list(request):

  videos = Video.objects.filter(isactive=1).order_by('-pub_date')
  headlines = Headline.objects.filter(isactive=1)

  variables = RequestContext(request, {
    'videos':videos,
    'headlines': headlines,
  })
  return render_to_response('video/list.html', variables)


def video_detail(request,slug):

  video = Video.objects.get(slug=slug)
  related_videos = video.related_videos.all()
  related_blogs = video.relatedblogs.all()
  related_links = video.relatedlinks.all()
  show = video.show
  headlines = Headline.objects.filter(isactive=1)

  variables = RequestContext(request, {
    'video': video,
    'related_videos':related_videos,
    'related_blogs': related_blogs,
    'related_links': related_links,
    'headlines': headlines,
    'show': show,
  })
  return render_to_response('video/detail.html', variables)
