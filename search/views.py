from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.db.models import Q
from search.forms import *
from video.models import *
from blog.models import *
from headlines.models import *
from shows.models import *
from django.db.models import Count
import itertools

def results(request):

    shows = Show.objects.filter(isactive=True)
    entries = {}
    videos = {}
    shows_results = {}
    search_result_total = 0

    if request.method == 'GET':
      return HttpResponseRedirect("/")

    search_string = request.POST.get("searchbox")
    if search_string:
      entries = Entry.objects.select_related().filter(
                  Q(title__icontains=search_string) |
                  Q(body_markdown__icontains=search_string),status=1)

      videos = Video.objects.select_related().filter(
                  Q(title__icontains=search_string) |
                  Q(details__icontains=search_string),isactive=1)

      shows_results = Show.objects.select_related().filter(
                  Q(title__icontains=search_string) |
                  Q(body_markdown__icontains=search_string),isactive=1)

    search_result_total = entries.count() + videos.count() + shows_results.count()

    search_results = itertools.chain(entries, videos, shows_results)

    headlines = Headline.objects.filter(isactive=1)
    variables = RequestContext(request, {
      'entries':entries,
      'videos':videos,
      'shows':shows,
      'search_result_total': search_result_total,
      'shows_results':shows_results,
      'search_results':search_results,
      'search_term':search_string,
      'headlines':headlines,
      #'tweets':tweets,
    })
    return render_to_response('search/results.html', variables)
