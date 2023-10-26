from django.db import models
from django.contrib.auth.models import User
from book.models import Book

class Account(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    username = models.CharField(max_length = 60)
    nama = models.CharField(max_length = 255 , default = "unknown")
    email = models.EmailField()
    buku_dibeli = models.ManyToManyField(Book, related_name='purchased')
    buku_ongoing = models.ManyToManyField(Book, related_name='ongoing_purchase')
    saldo = models.IntegerField()
    alamat = models.CharField(max_length = 1000)

class Review(models.Model):
    member = models.ForeignKey(Account, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    review_text = models.TextField()

class Admin(Account):
    orders_completed = models.IntegerField()
    books_added = models.IntegerField()




