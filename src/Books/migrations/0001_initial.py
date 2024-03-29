# Generated by Django 4.0.6 on 2022-08-13 21:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40, verbose_name='Categories')),
                ('slug', models.SlugField(max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('author', models.CharField(max_length=40)),
                ('summary', models.TextField()),
                ('cover_img', models.ImageField(blank=True, null=True, upload_to='img')),
                ('category', models.ManyToManyField(related_name='books', to='Books.category')),
            ],
        ),
    ]
