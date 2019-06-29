from django.views.generic import DetailView, CreateView, UpdateView, View, DeleteView, ListView, TemplateView
from django.urls import reverse, reverse_lazy
from webapp.models import UserInfo, Book, Bookmark, Author
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.shortcuts import redirect, render, get_object_or_404
from webapp.forms import BookForm, AuthorCreateForm

class BookListView(ListView):
    model = Book
    template_name = 'book_list.html'

    def get_queryset(self):
        return super().get_queryset().order_by('title')

class BookDetailView(DeleteView):
    model = Book
    template_name = 'book_detail.html'

class BookCreateView(PermissionRequiredMixin, LoginRequiredMixin, CreateView):
    model = Book
    template_name = 'book_create.html'
    form_class = BookForm
    permission_required = 'superuser'


class BookUpdateView(PermissionRequiredMixin, LoginRequiredMixin, UpdateView):
    model = Book
    template_name = 'book_update.html'
    form_class = BookForm
    permission_required = 'superuser'

    def get_success_url(self):
        return reverse('webapp:book_list')

class BookDeleteView(PermissionRequiredMixin, LoginRequiredMixin, DeleteView):
    model = Book
    permission_required = 'superuser'

def soft_delete_author(request, pk):
    author = get_object_or_404(Author, pk=pk)
    author.is_deleted = True
    author.save()
    return reverse('webapp:author_list')


class UserView(TemplateView, LoginRequiredMixin):
    template_name = "user_info.html"

    def dispatch(self, request, *args, **kwargs):
        if not UserInfo.objects.filter(user=request.user).exists():
            return redirect(reverse("edit_profile"))
        context = {
            'selected_user': request.user
        }
        return render(request, self.template_name, context)

class UserListView(ListView):
    model = UserInfo
    template_name = 'user_list.hmtl'

class AuthorListView(ListView):
    model = Author
    template_name = 'author_list.html'
    permission_required = 'superuser'

    def get_queryset(self):
        return Author.objects.filter(is_deleted=False)

class AuthorDetailView(DetailView):
    model = Author
    template_name = 'author_detail.html'


class AuthorDeleteView(PermissionRequiredMixin, LoginRequiredMixin, DeleteView):
    model = Author
    template_name = 'author_delete'
    permission_required = 'superuser'

class AuthorUpdateView(PermissionRequiredMixin, LoginRequiredMixin, UpdateView):
    model = Author
    template_name = 'author_update.html'
    form_class = AuthorCreateForm
    permission_required = 'superuser'

    def get_success_url(self):
        return reverse('webapp:author_list')


class AuthorCreateView(PermissionRequiredMixin, LoginRequiredMixin, CreateView):
    model = Author
    template_name = 'author_create.html'
    form_class = AuthorCreateForm
    permission_required = 'superuser'