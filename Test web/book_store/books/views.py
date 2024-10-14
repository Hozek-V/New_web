from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Books
from .forms import BookForm


class BookListView(ListView):
    model = Books
    template_name = 'book_list.html'


class BookDetailView(DetailView):
    model = Books
    template_name = 'book_detail.html'


class BookCreateView(LoginRequiredMixin, CreateView):
    model = Books
    form_class = BookForm
    template_name = 'book_form.html'
    success_url = reverse_lazy('book_list')


class BookUpdateView(LoginRequiredMixin, UpdateView):
    model = Books
    form_class = BookForm
    template_name = 'book_form.html'
    success_url = reverse_lazy('book_list')


class BookDeleteView(LoginRequiredMixin, DeleteView):
    model = Books
    template_name = 'book_confirm_delete.html'
    success_url = reverse_lazy('book_list')