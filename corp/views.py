from django.core.context_processors import request
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.template import RequestContext
from django.template.loader import get_template
from django.shortcuts import render_to_response
from corp.models import *
from headlines.models import Headline
from shows.models import Show

def about(request):

    content = Corporate.objects.get(section='about')
    variables = RequestContext(request, {
        'content':content
    })
    return render_to_response('corp/about.html', variables)


def privacy_policy(request):

    headlines = Headline.objects.filter(isactive=1)
    shows = Show.objects.filter(isactive=1)

    content = Corporate.objects.get(section='privacy')
    variables = RequestContext(request, {
        'content':content,
        'shows':shows,
        'headlines': headlines
    })
    return render_to_response('corp/privacy.html', variables)
