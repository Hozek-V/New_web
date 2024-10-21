from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Books
from .forms import BookForm
from .mixins import LoggingMixin


class BookListView(ListView):
    model = Books
    template_name = 'book_list.html'


class BookDetailView(DetailView, LoggingMixin):
    model = Books
    template_name = 'book_detail.html'

    def get(self, request, *args, **kwargs):
        self.log_action("Detail Book View")
        return super().get(request, *args, **kwargs)


class BookCreateView(LoginRequiredMixin, CreateView):
    model = Books
    form_class = BookForm
    template_name = 'book_form.html'
    success_url = reverse_lazy('book_list')


class BookUpdateView(LoginRequiredMixin, UpdateView, LoggingMixin):
    model = Books
    form_class = BookForm
    template_name = 'book_form.html'
    success_url = reverse_lazy('book_list')

    def form_valid(self, form):
        self.log_action("Update information")
        return super().form_valid(form)

    def get(self, request, *args, **kwargs):
        self.log_action("Load update form")
        return super().get(request, *args, **kwargs)


class BookDeleteView(LoginRequiredMixin, DeleteView):
    model = Books
    template_name = 'book_confirm_delete.html'
    success_url = reverse_lazy('book_list')