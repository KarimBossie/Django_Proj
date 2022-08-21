from django.shortcuts import render, get_object_or_404, redirect
from . import models
from Books.models import Book, Review, Author, Category
from django.views.generic import ListView
from django.contrib.auth.models import User


# Create your views here.

class BookListView(ListView):
    def get_queryset(self):
        return Book.objects.all()


def show(request, id):
    SingleBook = get_object_or_404(Book, pk=id)
    reviews = Review.objects.filter(book_id=id).order_by('-created_at')
    authors = Author.objects.filter()
    context = {'Books': SingleBook, 'reviews': reviews, 'authors': authors}
    return render(request, "Books/show.html", context)


def author(request, author):
    books = Book.objects.filter(authors__name=author)
    context = {'book_list': books}
    return render(request, 'Books/book_list.html', context)

def review(request, id):
    if request.user.is_authenticated:
        reviewsofthebook = request.POST['review']
        newReview = Review(reviewsofthebook=reviewsofthebook, book_id=id, user=request.user)
        newReview.save()
    return redirect('/book')