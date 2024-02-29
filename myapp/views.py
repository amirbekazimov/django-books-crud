from django.http import HttpResponse
from django.shortcuts import render
from .models import Book
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse

# Create your views here.
def hello_world(request):
    return HttpResponse("Hello, world!")

class BookListView(ListView):
    model = Book
    template_name = 'myapp/book_list.html' 

class BookDetailView(DetailView):
    model = Book
    template_name = 'myapp/book_detail.html' 


class BookCreateView(CreateView):
    model = Book
    template_name = 'myapp/book_form.html'
    fields = ['title', 'price', 'publish_date']  
    success_url = '/books/'

class BookUpdateView(UpdateView):
    model = Book
    fields = ['title', 'author', 'price', 'publish_date']
    template_name = 'myapp/book_form.html'

    def get_success_url(self):
        return reverse('book_detail', kwargs={'pk': self.object.pk})

class BookDeleteView(DeleteView):
    model = Book
    # template_name = 'myapp/book_form.html'
    success_url = '/books/'