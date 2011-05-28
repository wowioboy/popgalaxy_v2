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
from blog.models import *
from blog.forms import *
from video.models import *
from headlines.models import *
from shows.models import *

from django.contrib.auth.forms import UserCreationForm

import itertools

########################################
def home_page(request, section=None):

  data_range = 4
  #carousel_blog = Entry.objects.filter(status=1,carousel=1)[:data_range].values('carousel_text','carousel_subtext','slug','thumbnail')
  headlines = Headline.objects.filter(isactive=1)
  shows = Show.objects.filter(isactive=1)

  if section == 'comics':
    featured_videos = Video.objects.filter(isactive=1,featured=1,incomics=1)
    carousel_video = Video.objects.filter(isactive=1,carousel=1,incomics=1)
    latest_videos = Video.objects.filter(tags__icontains='comics')
    latest_blogs = Entry.objects.filter(status=1,tags__icontains='comics')
  elif section == 'music':
    featured_videos = Video.objects.filter(isactive=1,featured=1,inmusic=1)
    carousel_video = Video.objects.filter(isactive=1,carousel=1,inmusic=1)
    latest_videos = Video.objects.filter(tags__icontains='music')
    latest_blogs = Entry.objects.filter(status=1,tags__icontains='music')
  elif section == 'games':
    featured_videos = Video.objects.filter(isactive=1,featured=1,ingames=1)
    carousel_video = Video.objects.filter(isactive=1,carousel=1,ingames=1)
    latest_videos = Video.objects.filter(tags__icontains='games')
    latest_blogs = Entry.objects.filter(status=1,tags__icontains='games')
  elif section == 'film':
    featured_videos = Video.objects.filter(isactive=1,featured=1,infilm=1)
    carousel_video = Video.objects.filter(isactive=1,carousel=1,infilm=1)
    latest_videos = Video.objects.filter(tags__icontains='film')
    latest_blogs = Entry.objects.filter(status=1,tags__icontains='games')
  elif section == 'tv':
    featured_videos = Video.objects.filter(isactive=1,featured=1,intv=1)
    carousel_video = Video.objects.filter(isactive=1,carousel=1,intv=1)
    latest_videos = Video.objects.filter(tags__icontains='tv')
    latest_blogs = Entry.objects.filter(status=1,tags__icontains='tv')
  elif section == 'interactive':
    featured_videos = Video.objects.filter(isactive=1,featured=1,inint=1)
    carousel_video = Video.objects.filter(isactive=1,carousel=1,inint=1)
    latest_videos = Video.objects.filter(tags__icontains='interactive')
    latest_blogs = Entry.objects.filter(status=1,tags__icontains='interactive')
  elif section == 'extra':
    featured_videos = Video.objects.filter(isactive=1,featured=1,inextra=1)
    carousel_video = Video.objects.filter(isactive=1,carousel=1,inextra=1)
    latest_videos = Video.objects.filter(tags__icontains='extra')
    latest_blogs = Entry.objects.filter(status=1,tags__icontains='extra')
  else:
    featured_videos = Video.objects.filter(isactive=1,featured=1)
    carousel_video = Video.objects.filter(isactive=1,carousel=1)
    latest_videos = Video.objects.filter(isactive=1)
    latest_blogs = Entry.objects.filter(status=1)

  latest_videos = latest_videos.order_by('-pub_date')
  latest_blogs = latest_blogs.order_by('-pub_date')

  latest_items = itertools.chain(latest_blogs, latest_videos)

  
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
    'featured_videos':featured_videos,
    'carousel_video':carousel_video,
    'headlines':headlines,
    'tweets':tweets,
    'latest_videos': latest_videos,
    'latest_items': list(latest_items),
    'shows': shows,
    'category': section
  })
  return render_to_response('homepage.html',variables)


########################################
def blog(request):

  entries_range = 5
  entries = Entry.objects.filter(status=1).order_by('-pub_date', 'title')
  headlines = Headline.objects.filter(isactive=1)

  """
  auth = tweepy.OAuthHandler(settings.CONSUMER_KEY, settings.CONSUMER_SECRET)
  auth.set_access_token(settings.ACCESS_TOKEN, settings.ACCESS_SECRET)
  api = tweepy.API(auth)
  pop_timeline = api.user_timeline() # PG's timeline
  mentions = api.mentions()	# PG's @mentions
  dd_timeline = api.user_timeline('drunkduck') # DD's tweets
  wv_timeline = api.user_timeline('wevoltonline') # WEVolt's tweets
  tweets = {
    'pop_timeline':pop_timeline,
    'dd_timeline':dd_timeline,
    'wv_timeline':wv_timeline,
    'mentions':mentions
  }
  """
  variables = RequestContext(request, {
    'entries_range': range(entries_range),
    'entries': entries,
    'headlines':headlines,
  })
  return render_to_response('blog/index.html', variables)

########################################
def blog_entry(request, slug):

  entry = Entry.objects.filter(slug=slug)
  headlines = Headline.objects.filter(isactive=1)
  """
  auth = tweepy.OAuthHandler(settings.CONSUMER_KEY, settings.CONSUMER_SECRET)
  auth.set_access_token(settings.ACCESS_TOKEN, settings.ACCESS_SECRET)
  api = tweepy.API(auth)
  pop_timeline = api.user_timeline() # PG's timeline
  mentions = api.mentions()	# PG's @mentions
  dd_timeline = api.user_timeline('drunkduck') # DD's tweets
  wv_timeline = api.user_timeline('wevoltonline') # WEVolt's tweets
  tweets = {
    'pop_timeline':pop_timeline,
    'dd_timeline':dd_timeline,
    'wv_timeline':wv_timeline,
    'mentions':mentions
  }
  """


  variables = RequestContext(request,{
    'signup_form': UserCreationForm(),
    'entry':entry,
    'headlines':headlines,
  })
  return render_to_response('blog/entry.html',variables)
