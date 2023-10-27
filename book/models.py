from django.db import models
import random

class Book(models.Model):
    title = models.CharField(max_length=511, null=True)
    image = models.ImageField( upload_to='book/images', null=True, blank=True)
    authors = models.CharField(max_length=511, null=True)
    categories = models.CharField(max_length=511, null=True)
    price = models.IntegerField(default = random.randint(25000, 200000))
    description = models.TextField(default = "")
    no_of_pages = models.IntegerField(default = random.randint(100,1000))
    stock = models.IntegerField(default=0)
    rating = models.IntegerField(default=0)
    jumlah_terjual = models.IntegerField(default=0)
    
    
