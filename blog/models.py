  
from django.db import models
from django.utils import timezone


class Blog(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    image =models.ImageField(upload_to='blog/images/',max_length=300,blank=True)
    date = models.DateField(default=timezone.now())
    quote = models.TextField(blank=True)
    def __str__(self):
        return self.title

   
    
    
