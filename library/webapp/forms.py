import datetime
from django import forms
from webapp.models import Book, Author


class AuthorCreateForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = ['name', 'surname', 'birthdate', 'dateofdeath', 'photo', 'biography']
        widgets = {
            'birthdate': forms.SelectDateWidget(empty_label=('Год', 'Месяц', 'День'),
                                               years=[r for r in range(1970, datetime.date.today().year + 1)],
                                               attrs={
                                                   'class': 'form-control form-control-sm '
                                                            'shadow-none w-25 d-inline-block'}),
            'dateofdeath': forms.SelectDateWidget(empty_label=('Год', 'Месяц', 'День'),
                                               years=[r for r in range(1970, datetime.date.today().year + 1)],
                                               attrs={
                                                   'class': 'form-control form-control-sm '
                                                            'shadow-none w-25 d-inline-block',
                                                   'placeholder': 'Дата рождения', }),
            'name': forms.TextInput(
                attrs={'class': 'form-control form-control-sm shadow-none',
                       'placeholder': 'Имя'}),
            'surname': forms.TextInput(
                attrs={'class': 'form-control form-control-sm shadow-none',
                       'placeholder': 'Фамилия'}),
            'biography': forms.Textarea(attrs={'class': 'form-control form-control-sm shadow-none',
                                               'placeholder': 'Биография  ', 'rows': '4'}),
        }


class BookForm(forms.ModelForm):
    author = forms.ModelChoiceField(queryset=Author.objects.filter(is_deleted=False),
                                    empty_label='Неизвестен',
                                    widget=forms.Select
                                    (attrs={'class': 'form-control form-control-sm shadow-none', }),
                                    label='Автор', required=False)

    class Meta:
        model = Book
        fields = ['title', 'author', 'cover', 'file', 'publicationdate', 'description']
        widgets = {
            'name': forms.TextInput(
                attrs={'class': 'form-control form-control-sm shadow-none',
                       'placeholder': 'Название книги'}),
            'created_date': forms.TextInput(
                attrs={'class': 'form-control form-control-sm shadow-none',
                       'placeholder': 'Дата публикации'}),
            'description': forms.TextInput(
                attrs={'class': 'form-control form-control-sm shadow-none',
                       'placeholder': 'Описание'}),
        }