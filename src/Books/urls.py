from importlib.resources import path
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('<int:id>', views.show, name='book.show'),
    path('review', views.review, name='book.review'),
]