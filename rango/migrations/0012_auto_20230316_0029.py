# Generated by Django 2.1.5 on 2023-03-16 00:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rango', '0011_auto_20230316_0023'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='slug',
            field=models.SlugField(unique=True),
        ),
    ]
