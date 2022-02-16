from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from .models import Authors, Books
from django.views.generic import CreateView, ListView, DeleteView, UpdateView
from .forms import BooksCreateViewForm


class BooksListView(ListView):
    model = Books
    template_name = 'books.html'
    queryset = Books.objects.all()[:5]


class BooksCreateView(CreateView):
    model = Books
    form_class = BooksCreateViewForm
    template_name = 'add-books.html'
    success_url = reverse_lazy('books:books_list')
    

class BooksUpdateView(UpdateView):
    model = Books
    form_class = BooksCreateViewForm
    template_name = 'update-books.html'
    success_url = reverse_lazy('books:books_list')

class BooksDeleteView(DeleteView):
    model = Books
    template_name = 'delete-books.html'
    success_url = reverse_lazy('books:books_list')