from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    price = models.IntegerField()
    rating = models.IntegerField(default=0)
    # add more, don't forget to migrate
