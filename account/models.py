from django.db import models
from django.contrib.auth.models import User
from book.models import Book
from django.db.models.signals import post_save
from django.dispatch import receiver

class Account(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    nama = models.CharField(max_length = 255 , blank=True)
    email = models.EmailField(blank=True)
    buku_dibeli = models.ManyToManyField(Book, related_name='purchased', blank=True)
    buku_ongoing = models.ManyToManyField(Book, related_name='ongoing_purchase', blank=True)
    saldo = models.IntegerField(default=0)
    alamat = models.CharField(max_length = 1000, default="-", blank=True, null=True)

@receiver(post_save, sender=User)
def create_user_account(sender, instance, created, **kwargs):
    if created:
        Account.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_account(sender, instance, **kwargs):
    try:
        _ = (instance.account is not None)
    except Account.DoesNotExist:
        return
    instance.account.save()

    
class Review(models.Model):
    member = models.ForeignKey(Account, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    review_text = models.TextField()
