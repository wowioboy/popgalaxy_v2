from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render_to_response
from django.template import RequestContext
from comments.models import Comment
from comments.forms import CommentForm
from video.models import *

@login_required
def add_comment(request, object_type, id):
    
    skip = False
    if object_type == 'comicpage':
        object = get_object_or_404(ComicPage, pk=id)
    elif object_type == 'article':
        object = get_object_or_404(Article, pk=id)
    elif object_type == 'profile':
        object = get_object_or_404(Profile, pk=id)
        friend_status = get_relationship_status(object.user, request.user)
        if friend_status < 2 and object.user != request.user:
            skip = True
    elif object_type == 'tutorial': 
        object = get_object_or_404(Tutorial, pk=id)
    elif object_type == 'episode': 
        object = get_object_or_404(Episode, pk=id)
    elif object_type == 'video': 
        object = get_object_or_404(Video, pk=id)
    if request.method == 'POST' and not skip:
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.author = request.user
            comment.save()
            object.comments.add(comment)
    comments = object.comments.filter(is_deleted=False)
    return render_to_response('comments/list.html', {'comments':comments}, context_instance=RequestContext(request))

@login_required
def get_comments(request, object_type, id):
    
    user = None
    if object_type == 'comicpage':
        object = get_object_or_404(ComicPage, pk=id)
        user = object.comic.user
    elif object_type == 'article':
        object = get_object_or_404(Article, pk=id)
        user = object.author
    elif object_type == 'profile':
        object = get_object_or_404(Profile, pk=id)
    elif object_type == 'tutorial': 
        object = get_object_or_404(Tutorial, pk=id)
    elif object_type == 'episode': 
        object = get_object_or_404(Episode, pk=id)
    elif object_type == 'video': 
        object = get_object_or_404(Video, pk=id)
    if not user:
        user = object.user
    if request.GET.get('delete', False):
        comment = Comment.objects.get(pk=request.GET['delete'])
        if comment.author == request.user or user == request.user or request.user.is_staff:
            comment.is_deleted = True
            comment.save()
    comments = object.comments.filter(is_deleted=False)
    return render_to_response('comments/list.html', {'comments':comments}, context_instance=RequestContext(request))
