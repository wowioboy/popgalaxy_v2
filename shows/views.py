import tweepy
import itertools
from django.template import RequestContext
from django.shortcuts import render_to_response
from django.conf import settings
from shows.models import *
from headlines.models import *


########################################
def show_page(request, slug='shegeek'):

    headlines = Headline.objects.filter(isactive=1)
    shows = Show.objects.filter(isactive=1)

    selected_show = Show.objects.get(isactive=1,slug=slug)
    related_videos = selected_show.relatedvideos.all()
    related_blogs = selected_show.relatedblogs.all()
    featured_videos = selected_show.relatedvideos.filter(featured=True)

    related_videos = related_videos.order_by('-pub_date')
    sidebar_videos = related_videos.order_by('pub_date')[:4]
    related_blogs = related_blogs.order_by('-pub_date')
    featured_videos = featured_videos.order_by('-pub_date')

    latest_items = itertools.chain(related_blogs, related_videos)

  
    tweets = {}
    auth = tweepy.OAuthHandler(settings.CONSUMER_KEY, settings.CONSUMER_SECRET)
    auth.set_access_token(settings.ACCESS_TOKEN, settings.ACCESS_SECRET)
    api = tweepy.API(auth)
    try:
      pop_timeline = api.user_timeline(count=100) # PG's timeline
    except:
      pop_timeline = []
    tweets = {
      'pop_timeline':pop_timeline,
    }
  
    variables = RequestContext(request,{
      'related_blogs':related_blogs,
      'headlines':headlines,
      'tweets':tweets,
      'related_videos': related_videos,
      'sidebar_videos': sidebar_videos,
      'featured_videos': featured_videos,
      'latest_items': list(latest_items),
      'shows': shows,
      'selected_show': selected_show
    })
    return render_to_response('shows/index.html',variables)
