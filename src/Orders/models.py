from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
from Books.models import Book

# Create your models here.

class Order(models.Model):
    users = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    item = models.ForeignKey(Book, on_delete=models.CASCADE, null=True)
    quantity = models.IntegerField(default=0)
    added = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return str(self.item)