from Orders import views
from django.urls import path

urlpatterns = [
    path('', views.order, name="order"),
    path('order_add/<id>', views.order_add, name = 'order-add'),
]
