# Generated by Django 4.0.6 on 2022-08-13 22:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Books', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='slug',
        ),
    ]
