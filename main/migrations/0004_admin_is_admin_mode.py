# Generated by Django 4.2.6 on 2023-10-28 23:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='admin',
            name='is_admin_mode',
            field=models.BooleanField(default=True),
        ),
    ]