from django.db import models
import datetime
# Create your models here.

class Post (models.Model):
    title=models.TextField()
    image=models.ImageField(upload_to='blog/')
    full_story =models.TextField()
    date = models.DateField(("Date"), default=datetime.date.today)

    def __str__(self):
        return self.title

    def summary (self):
        return self.full_story[:100]+" ..."