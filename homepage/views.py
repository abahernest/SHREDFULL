from django.shortcuts import render
from .models import Background

# Create your views here.

def HomeView (requests):
    
    return render(requests, 'homepage/index.html') #{'background':bg})
