# Generated by Django 4.2.5 on 2023-10-28 13:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0033_alter_book_no_of_pages_alter_book_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='no_of_pages',
            field=models.IntegerField(default=371),
        ),
        migrations.AlterField(
            model_name='book',
            name='price',
            field=models.IntegerField(default=88711),
        ),
    ]