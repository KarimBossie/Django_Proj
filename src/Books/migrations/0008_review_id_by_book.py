# Generated by Django 4.0.6 on 2022-08-14 17:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Books', '0007_review_created_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='id_by_book',
            field=models.BigIntegerField(default=1),
        ),
    ]