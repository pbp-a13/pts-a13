# Generated by Django 4.2.6 on 2023-10-16 03:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('image', models.ImageField(upload_to='images/')),
                ('author', models.CharField(max_length=255)),
                ('price', models.IntegerField()),
                ('rating', models.IntegerField()),
            ],
        ),
    ]