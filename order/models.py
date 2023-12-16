from django.db import models
from django.contrib.auth.models import User
from book.models import Book

# Create your models here.
class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    books = models.ManyToManyField(Book)
    quantity = models.PositiveIntegerField()
    is_completed = models.BooleanField(default=False)
    order_date = models.DateTimeField(auto_now_add=True)
