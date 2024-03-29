from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from Books import views


urlpatterns = [
    path('book/', include('Books.urls')),
    path('admin/', admin.site.urls),
    path('login/', auth_views.LoginView.as_view(redirect_authenticated_user=True)),
    path('', include('django.contrib.auth.urls')),
    path('about/', views.about, name='about'),
    path("register/", views.signup, name="register"),
]
