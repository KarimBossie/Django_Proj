from django.db import models
from django.forms import IntegerField

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length = 40)
    def __str__(self) -> str:
        return self.name

class Book(models.Model):
    title = models.CharField(max_length = 100)
    author = models.CharField(max_length = 40)
    pagecount = models.IntegerField(null=True)
    price = models.IntegerField(null=True)
    summary = models.TextField()
    cover_img = models.ImageField(upload_to = 'img', blank = True, null = True)
    category = models.ManyToManyField(Category)
    def __str__(self) -> str:
        return self.title


class Review(models.Model):
    reviewsofthebook = models.TextField()
