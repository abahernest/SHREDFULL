from django.shortcuts import render
from .models import Post
from django.views.decorators.cache import cache_page


# Create your views here.
@cache_page (60*5)
def PostView(requests):
    PS=Post.objects
    return render(requests, 'blog/home.html', {'posts':PS})