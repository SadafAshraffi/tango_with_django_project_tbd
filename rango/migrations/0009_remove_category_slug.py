# Generated by Django 2.1.5 on 2023-03-15 23:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rango', '0008_auto_20230315_2246'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='slug',
        ),
    ]
