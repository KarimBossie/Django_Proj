# Generated by Django 4.0.6 on 2022-08-16 10:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Books', '0011_author_delete_authors_alter_book_authors'),
    ]

    operations = [
        migrations.CreateModel(
            name='Authors',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.CharField(max_length=100)),
                ('created_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.DeleteModel(
            name='Author',
        ),
        migrations.AlterField(
            model_name='book',
            name='authors',
            field=models.ManyToManyField(to='Books.authors'),
        ),
    ]
