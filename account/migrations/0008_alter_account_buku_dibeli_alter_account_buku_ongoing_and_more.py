# Generated by Django 4.2.6 on 2023-10-27 14:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0025_alter_book_no_of_pages_alter_book_price'),
        ('account', '0007_alter_account_buku_dibeli_alter_account_buku_ongoing_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='buku_dibeli',
            field=models.ManyToManyField(blank=True, related_name='purchased', to='book.book'),
        ),
        migrations.AlterField(
            model_name='account',
            name='buku_ongoing',
            field=models.ManyToManyField(blank=True, related_name='ongoing_purchase', to='book.book'),
        ),
        migrations.AlterField(
            model_name='account',
            name='email',
            field=models.EmailField(blank=True, max_length=254),
        ),
    ]
