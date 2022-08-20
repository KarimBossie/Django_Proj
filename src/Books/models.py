from django.db import models
from django.forms import IntegerField
from django.contrib.auth.models import User

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length = 40)
    def __str__(self) -> str:
        return self.name

class Author(models.Model):
    name = models.CharField(max_length = 100)
    created_at = models.DateTimeField(auto_now=True)
    def __str__(self) -> str:
        return self.name

class Book(models.Model):
    title = models.CharField(max_length = 100)
    authors = models.ManyToManyField(Author)
    pagecount = models.IntegerField(null=True)
    price = models.IntegerField(null=True)
    summary = models.TextField()
    cover_img = models.ImageField(upload_to = 'img', blank = True, null = True)
    category = models.ManyToManyField(Category)
    def __str__(self) -> str:
        return self.title


class Review(models.Model):
    reviewsofthebook = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    created_at = models.DateTimeField(auto_now=True)
    book_id = models.BigIntegerField(default=1)
    