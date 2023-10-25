from django.db import models
import random

class Book(models.Model):
    title = models.CharField(max_length=511, null=True)
    authors = models.CharField(max_length=511, null=True)
    categories = models.CharField(max_length=511, null=True)
    
