# Generated by Django 4.0.6 on 2022-08-14 09:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Books', '0002_remove_category_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='pagecount',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='book',
            name='price',
            field=models.IntegerField(null=True),
        ),
    ]
