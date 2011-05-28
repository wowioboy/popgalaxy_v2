import tweepy
from django.db.models import Q
from django.core.exceptions import ObjectDoesNotExist
from django.db import connection
from django.core import serializers
from django.utils import encoding
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.template import RequestContext
from django.contrib.auth.models import User
from django.contrib.auth import logout
from django.template.loader import get_template
from django.shortcuts import render_to_response
from django.conf import settings
from itertools import chain
from shows.models import *

import itertools

########################################
def show_page(request, slug='shegeek'):

    data_range = 4
    #carousel_blog = Entry.objects.filter(status=1,carousel=1)[:data_range].values('carousel_text','carousel_subtext','slug','thumbnail')
    headlines = Headline.objects.filter(isactive=1)
    shows = Show.objects.filter(isactive=1)

    selected_show = Show.objects.get(isactive=1,featured=1,slug=slug)
    related_videos = selected_show.relatedvideos.all()
    related_blogs = selected_show.relatedblogs.all()

    related_videos = related_videos.order_by('-pub_date')
    related_blogs = related_blogs.order_by('-pub_date')

    latest_items = itertools.chain(related_blogs, related_videos)

  
    tweets = {}
    auth = tweepy.OAuthHandler(settings.CONSUMER_KEY, settings.CONSUMER_SECRET)
    auth.set_access_token(settings.ACCESS_TOKEN, settings.ACCESS_SECRET)
    api = tweepy.API(auth)
    try:
      pop_timeline = api.user_timeline(count=100) # PG's timeline
      #mentions = api.mentions()	# PG's @mentions
      #dd_timeline = api.user_timeline('drunkduck') # DD's tweets
      #wowio_timeline = api.user_timeline('wowio') # WOWIO's tweets
      #wv_timeline = api.user_timeline('wevoltonline') # WEVolt's tweets
    except:
      pop_timeline = []
      #dd_timeline = []
      #wowio_timeline = []
      #wv_timeline = []
    tweets = {
      'pop_timeline':pop_timeline,
      #'dd_timeline':dd_timeline,
      #'wv_timeline':wv_timeline,
      #'wowio_timeline':wowio_timeline,
      #'mentions':mentions
    }
  
    variables = RequestContext(request,{
      'related_blogs':related_blogs,
      'headlines':headlines,
      'tweets':tweets,
      'related_videos': related_videos,
      'latest_items': list(latest_items),
      'shows': shows,
      'selected_show': selected_show
    })
    return render_to_response('shows/index.html',variables)
