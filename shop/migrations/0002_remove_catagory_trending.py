# Generated by Django 5.1.4 on 2024-12-18 16:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='catagory',
            name='trending',
        ),
    ]
