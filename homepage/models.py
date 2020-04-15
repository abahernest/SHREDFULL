from django.db import models

class Background (models.Model):
    image =models.ImageField(upload_to='img/')
    text = models.CharField(max_length=300)

    def __str__(self):
        return self.text