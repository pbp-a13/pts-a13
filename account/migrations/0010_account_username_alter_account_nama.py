# Generated by Django 4.2.6 on 2023-10-29 06:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0009_delete_admin'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='username',
            field=models.CharField(default=1, max_length=255),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='account',
            name='nama',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]