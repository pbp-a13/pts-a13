# Generated by Django 4.2.6 on 2023-10-28 23:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0028_alter_book_no_of_pages_alter_book_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='no_of_pages',
            field=models.IntegerField(default=474),
        ),
        migrations.AlterField(
            model_name='book',
            name='price',
            field=models.IntegerField(default=130723),
        ),
    ]
