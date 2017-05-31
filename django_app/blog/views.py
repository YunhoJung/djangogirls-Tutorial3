from django.http import HttpResponse
from django.shortcuts import render
from .models import Post
from django.utils import timezone

def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now())
    context = {
        'title': 'SEOUL TIMES',
        'posts': posts
    }
    return render(request, 'blog/post_list.html', context=context)

