# Generated by Django 4.2.6 on 2023-10-29 09:40

from django.db import migrations
from django.core.management import call_command

def load_my_initial_data(apps, schema_editor):
    call_command("loaddata", "books.json")


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0035_alter_book_no_of_pages_alter_book_price'),
    ]

    operations = [
        migrations.RunPython(load_my_initial_data),
    ]