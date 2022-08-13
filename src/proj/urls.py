from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('book/', include('Books.urls')),
    path('admin/', admin.site.urls), 
]
