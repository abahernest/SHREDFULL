from django.shortcuts import render
from django.views.decorators.cache import cache_page
from .models import Background

# Create your views here.
@cache_page(60 *30)
def HomeView (requests):
    bg =Background.objects

    return render(requests, 'homepage/index.html', {'background':bg})
@cache_page(60*60)
def AboutView (requests):
    return render(requests,'homepage/about-us.html')

@cache_page(60*60)
def StoreView (requests):
    return render (requests,'homepage/store_home.html')
