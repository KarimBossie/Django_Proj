from django.contrib import admin
from Books import models

# Register your models here.

admin.site.register(models.Category)
admin.site.register(models.Book)
admin.site.register(models.Review)
admin.site.register(models.Author)