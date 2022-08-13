from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField("Categories", max_length = 40)
    def __str__(self) -> str:
        return self.name

class Book(models.Model):
    title = models.CharField(max_length = 100)
    author = models.CharField(max_length = 40)
    summary = models.TextField()
    cover_img = models.ImageField(upload_to = 'img', blank = True, null = True)
    category = models.ManyToManyField(Category, related_name='books')
    def __str__(self) -> str:
        return self.title