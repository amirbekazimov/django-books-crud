"""
URL configuration for myproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from myapp.views import hello_world
from myapp import views
from myapp.views import BookDetailView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('hello/', hello_world),
    path('books/', views.BookListView.as_view(), name='book_list'),
    path('book/<int:pk>/', BookDetailView.as_view(), name='book_detail'),
    path('book/new/', views.BookCreateView.as_view(), name='book_new'),
    path('book/<int:pk>/edit/', views.BookUpdateView.as_view(), name='book_edit'),
    path('book/<int:pk>/delete/', views.BookDeleteView.as_view(), name='book_delete'),
]
