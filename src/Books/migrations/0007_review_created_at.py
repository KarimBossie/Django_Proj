# Generated by Django 4.0.6 on 2022-08-14 17:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Books', '0006_rename_reviews_review'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='created_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
