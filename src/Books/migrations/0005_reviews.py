# Generated by Django 4.0.6 on 2022-08-14 14:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Books', '0004_alter_book_category_alter_category_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Reviews',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reviewsofthebook', models.TextField()),
            ],
        ),
    ]
