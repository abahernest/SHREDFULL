from django.shortcuts import render
from .models import Post



# Create your views here.
def PostView(requests):
    PS=Post.objects
    return render(requests, 'blog/home.html', {'posts':PS})