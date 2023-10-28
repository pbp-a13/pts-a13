# Generated by Django 4.2.6 on 2023-10-27 06:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0015_book_image_alter_book_no_of_pages_alter_book_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='book/images'),
        ),
        migrations.AlterField(
            model_name='book',
            name='no_of_pages',
            field=models.IntegerField(default=946),
        ),
        migrations.AlterField(
            model_name='book',
            name='price',
            field=models.IntegerField(default=33881),
        ),
    ]
