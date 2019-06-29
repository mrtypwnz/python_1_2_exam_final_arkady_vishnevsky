from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Author(models.Model):
    name = models.CharField(max_length=55, verbose_name="Имя")
    surname = models.CharField(max_length=55, verbose_name="Фамилия")
    birthdate = models.DateField(blank=True, verbose_name="Дата рождения")
    dateofdeath = models.DateField(blank=True, verbose_name="Дата смерти")
    biography = models.TextField(blank=True, verbose_name="Биография")
    photo = models.ImageField(blank=True, verbose_name="Фотография")
    status = models.BooleanField(default=True)

class Book(models.Model):
    title = models.CharField(max_length=55, verbose_name='Название')
    author = models.ForeignKey(Author, on_delete=models.PROTECT)
    publicationdate = models.DateField()
    file = models.FileField()
    cover = models.ImageField(blank=True, verbose_name="Обложка")
    description = models.TextField(max_length=2500, blank=True, verbose_name="Описание")

class Bookmark(models.Model):
    bookmark_id = models.AutoField(primary_key=True)
    user = models.OneToOneField(User, on_delete=models.PROTECT, related_name='bookmarks')
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='bookmarks')

class UserInfo(models.Model):
    user = models.OneToOneField(User, on_delete=models.PROTECT, verbose_name="Пользователь")
    avatar = models.FileField(null=True, blank=True, verbose_name="Аватар")
    phone_number = models.CharField(max_length=15, verbose_name="Номер телефона")
    bookmarks = models.ManyToManyField(Bookmark, blank=True, related_name='bookmarks', verbose_name='Закладки')