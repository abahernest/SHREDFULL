from django.shortcuts import render
from .models import Background

# Create your views here.

def HomeView (requests):
    bg =Background.objects

    return render(requests, 'homepage/index.html', {'background':bg})

def AboutView (requests):
    return render(requests,'homepage/about-us.html')


def StoreView (requests):
    return render (requests,'homepage/store_home.html')
