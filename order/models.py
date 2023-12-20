from django.db import models
from django.contrib.auth.models import User
from book.models import Book

# Create your models here.
class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=0)
    is_completed = models.BooleanField(default=False)
    order_date = models.DateTimeField(auto_now_add=True)
