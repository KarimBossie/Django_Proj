# Generated by Django 4.0.6 on 2022-08-18 15:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('DjanGoBookStoRe', '0005_city_region'),
    ]

    operations = [
        migrations.DeleteModel(
            name='City',
        ),
        migrations.DeleteModel(
            name='Region',
        ),
    ]