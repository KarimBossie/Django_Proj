from importlib.resources import path
from django.urls import path
from . import views

urlpatterns = [
    path('', views.BookListView.as_view(), name='book.all'), #views.home),
    path('<int:id>', views.show, name='book.show'),
    path('<int:id>/review', views.review, name='book.review'),
    path('<str:author>', views.author, name="author.books"),
    #path('about', about.html, name='about'),
]