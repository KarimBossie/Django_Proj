from tabnanny import verbose
from django.db import models

# Create your models here.


class City(models.Model):
    name = models.CharField(
        verbose_name="city's name",
        max_length=25
        )
    description = models.TextField(
        verbose_name="city's name",
        blank=True,
        null=True
    )