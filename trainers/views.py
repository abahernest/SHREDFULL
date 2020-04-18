from django.shortcuts import render
from .models import Trainer,GymAgency
from django.views.decorators.cache import cache_page
# Create your views here.

@cache_page (60*5)
def TrainerView (requests):
    TR=Trainer.objects
    return render (requests, 'trainers/trainers.html',{'trainer':TR})
@cache_page (60*5)
def GymAgencyView (requests):
    GY=GymAgency.objects
    return render (requests, 'trainers/gymCenters.html',{'agency':GY})

