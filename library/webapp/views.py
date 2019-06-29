from django.views.generic import DetailView, CreateView, UpdateView, View, DeleteView, ListView, TemplateView
from django.urls import reverse, reverse_lazy
from webapp.models import UserInfo, Book, Bookmark, Author
from webapp.forms import PostForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect, render, get_object_or_404


class BookListView(ListView):
    model = Book
    template_name = 'book_list.html'

    def get_queryset(self):
        return super().get_queryset().order_by('name')
