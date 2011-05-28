from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from search.forms import *
from video.models import *
from django.db.models import Count
from datetime import datetime, date, timedelta

def results(request):
    
    search = None
    comics = Comic.objects.filter(is_deleted=False, pages__post_date__lte=datetime.now()).annotate(count=Count('title'))
    if request.GET.values():
        form = SearchForm(request.GET)
        
        if request.GET.get('pages', False):
            pages = request.GET['pages']
            comics = comics.annotate(page_count=Count('pages'))
            if pages == '2':
                comics = comics.filter(page_count__gte=2)
            elif pages == '10':
                comics = comics.filter(page_count__gte=10)
            elif pages == '50':
                comics = comics.filter(page_count__gte=50)
            elif pages == 'r':
                if request.GET.get('page_min', False):
                    comics = comics.filter(page_count__gte=int(request.GET['page_min']))
                if request.GET.get('page_max', False):
                    comics = comics.filter(page_count__lte=int(request.GET['page_max']))
                    
        if request.GET.get('search', False):
            search = request.GET['search'].strip()
            if search != 'search':
                comics = comics.filter(title__icontains=search) | comics.filter(description__icontains=search) | comics.filter(user__username__icontains=search)
            else:
                search = None
            
        if 'style' in request.GET:
            comics = comics.filter(style__in=request.GET.getlist('style'))
        if 'genre' in request.GET:
            comics = comics.filter(genre__in=request.GET.getlist('genre'))
        if 'tone' in request.GET:
            comics = comics.filter(tone__in=request.GET.getlist('tone'))
        if 'type' in request.GET:
            comics = comics.filter(type__in=request.GET.getlist('type'))
        if 'rating' in request.GET:
            comics = comics.filter(rating__in=request.GET.getlist('rating'))
        
        if request.GET.get('last_update', False):
            update = request.GET['last_update']
            today = date.today()
            if update == 'today':
                comics = comics.filter(date_modified__year=today.year).filter(date_modified__month=today.month).filter(date_modified__day=today.day)
            elif update == 'week':
                days = timedelta(days=7)
                begin = today - days
                comics = comics.filter(date_modified__range=(begin, today))
            elif update == 'month':
                days = timedelta(days=30)
                begin = today - days
                comics = comics.filter(date_modified__range=(begin, today))
                    
    else:
        form = SearchForm()
        comics = comics.annotate(like_count=Count('likes')).order_by('-like_count')
    return render_to_response('search/index.html', {'comics': comics, 'form':form, 'search':search}, context_instance=RequestContext(request))
