from django.db import models

# Create your models here.
class Trainer (models.Model):
    Name=models.CharField(max_length=300)
    image=models.ImageField(upload_to='trainers/')
    age=models.IntegerField()
    Mobile= models.BigIntegerField()
    Email=models.EmailField()
    Experience=models.IntegerField(help_text='enter years of gym or coaching experience')
    SPECIALTY_CHOICES=[('Yoga','Yoga'),('Body Building','Body Building'),('Dieting','Dieting')]
    Specialty= models.TextField(choices=SPECIALTY_CHOICES)
    PER=[('Daily','Daily'),('Weekly','Weekly'),('Monthly','Monthly'),('Quarterly','Quarterly'),('Yearly','Yearly')]
    Per_time = models.TextField(choices=PER)
    service= models.TextField(help_text='enter various services you offer separated by comma (,)')
    Pricing = models.IntegerField(help_text='how much do you charge by duration')
    
    def __str__(self):
        return self.Name


class GymAgency (models.Model):
    Name=models.CharField(max_length=300)
    image=models.ImageField(upload_to='gymcenters/')
    location=models.TextField()
    Mobile= models.BigIntegerField()
    Email=models.EmailField()
    experience=models.IntegerField()
    Subscription=models.IntegerField()
    PER=[('Daily','Daily'),('Weekly','Weekly'),('Monthly','Monthly'),('Quarterly','Quarterly'),('Yearly','Yearly')]
    Per_time = models.TextField(choices=PER)
    service= models.TextField(help_text='enter various services you offer separated by comma (,)')


    def __str__(self):
        return self.Name