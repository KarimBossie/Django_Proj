from tabnanny import verbose
from django.db import models

# Create your models here.


class City(models.Model):
    region = models.ForeignKey(
        "DjanGoBookStoRe.Region",
        on_delete=models.PROTECT,
        verbose_name="Region",
        related_name="Cities"
    )
    name = models.CharField(
        verbose_name="City's name",
        max_length=25
        )
    post_index = models.IntegerField(
        verbose_name="Post Index"
        )
    description = models.TextField(
        verbose_name="City's description",
        blank=True,
        null=True
    )
    def __str__(self) -> str:
        return str(self.pk) + ". " + self.name

class Region(models.Model):
    name = models.CharField(
        verbose_name="Region's name",
        max_length=30
        )
    description = models.TextField(
        verbose_name="Region's description",
        blank=True,
        null=True
    )
    def __str__(self) -> str:
        return str(self.pk) + ". " + self.name