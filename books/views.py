from django.shortcuts import render
from django.views import generic
from django.urls import reverse_lazy

from .models import Book


class BookListView(generic.ListView):
    model = Book
    paginate_by = 4
    template_name = 'books/book_list.html'
    context_object_name = 'books'


class BookDetailView(generic.DetailView):
    model = Book
    template_name = 'books/book_detail.html'


class BookCreateView(generic.edit.CreateView):
    model = Book
    fields = ['title', 'author', 'description', 'price','cover']
    template_name = 'books/book_create.html'


class BookUpdateView(generic.edit.UpdateView):
    model = Book
    fields = ['title', 'author', 'description', 'price','cover']
    template_name = 'books/book_update.html'


class BookDeleteView(generic.DeleteView):
    model = Book
    template_name = 'books/book_delete.html'
    success_url = reverse_lazy ('book_list')




# Create your views here.
