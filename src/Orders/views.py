from django.shortcuts import render, redirect
from .models import Order
from Books.models import Book

# Create your views here.

def order(request):
   order = Order.objects.filter(users=request.user)
   context = {'order':order}
   return render(request, 'Orders/order.html', context)

def order_add(request, id):
    book = Book.objects.get(pk=id)
    orders = Order.objects.create(users=request.user, item=book)
    orders.save()
    return redirect('/book')