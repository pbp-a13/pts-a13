# Generated by Django 4.2.6 on 2023-10-16 06:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0002_alter_book_image_alter_book_rating'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='image',
            field=models.ImageField(blank=True, default='Toko_Buku/media/book/images/placeholder.png', upload_to='book/images'),
        ),
    ]