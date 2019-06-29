from django.urls import path
from webapp.views import BookListView, UserView, BookDetailView, BookDeleteView, BookCreateView, AuthorCreateView, AuthorDetailView, AuthorListView, BookUpdateView, AuthorDeleteView, AuthorUpdateView

app_name = 'webapp'

urlpatterns = [
    path('', BookListView.as_view(), name='book_list'),
    path('book/<int:pk>', BookDetailView.as_view(), name='book_detail'),
    path('book/<int:pk>', BookUpdateView.as_view(), name='book_update'),
    path('book/create/', BookCreateView.as_view(), name='book_create'),
    path('book/<int:pk>', BookDeleteView.as_view(), name='book_delete'),
    path('authors/<int:pk>', AuthorUpdateView.as_view(), name='author_update'),
    path('authors/<int:pk>', AuthorDeleteView.as_view(), name='author_delete'),
    path('users/<int:pk>', UserView.as_view(), name='user_info'),
    path('authors/<int:pk>', AuthorDetailView.as_view(), name='author_detail'),
    path('authors/create/', AuthorCreateView.as_view(), name='author_create'),
    path('authors/', AuthorListView.as_view(), name='author_list')
]