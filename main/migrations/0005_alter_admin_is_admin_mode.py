# Generated by Django 4.2.6 on 2023-10-29 07:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_admin_is_admin_mode'),
    ]

    operations = [
        migrations.AlterField(
            model_name='admin',
            name='is_admin_mode',
            field=models.BooleanField(),
        ),
    ]