# Generated by Django 4.2.6 on 2023-10-29 12:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book_info', '0009_alter_cart_member'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cart',
            old_name='member',
            new_name='user',
        ),
        migrations.RemoveField(
            model_name='cart',
            name='jumlah_pembelian',
        ),
        migrations.AddField(
            model_name='cart',
            name='amount',
            field=models.PositiveIntegerField(default=1),
        ),
    ]
