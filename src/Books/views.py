from django.shortcuts import render, get_object_or_404, redirect
from . import models
from Books.models import Book, Review


# Create your views here.

def home(request):
    dbData = Book.objects.all()
    context = {'Books': dbData}
    return render(request, 'Books/startpage.html', context)

def show(request, id):
    SingleBook = get_object_or_404(Book, pk=id)
    context = {'Books': SingleBook}
    return render(request, "Books/show.html", context)


def review(request):
    bodyofreview = request.POST['Review']
    newReview = Review(bodyofreview=bodyofreview)
    newReview.save()
    return redirect('/book')