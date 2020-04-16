from django.shortcuts import render
from .models import Trainer,GymAgency

# Create your views here.

def TrainerView (requests):
    TR=Trainer.objects
    return render (requests, 'trainers/trainers.html',{'trainer':TR})

def GymAgencyView (requests):
    GY=GymAgency.objects
    return render (requests, 'trainers/gymCenters.html',{'agency':GY})

