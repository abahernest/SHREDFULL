"""The_Pit URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from homepage.views import HomeView,AboutView,StoreView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('abahjnr/', admin.site.urls),
    path('', HomeView, name='home'),
    path('about/', AboutView,name='about'),
    path('store/', StoreView, name='store'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

