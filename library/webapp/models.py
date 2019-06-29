from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class SoftDeleteManager(models.Manager):
    def active(self):
        return self.filter(is_deleted=False)

    def deleted(self):
        return self.filter(is_deleted=True)

class Author(models.Model):
    name = models.CharField(max_length=55, verbose_name="Имя")
    surname = models.CharField(max_length=55, verbose_name="Фамилия")
    birthdate = models.DateField(null=True, blank=True, verbose_name="Дата рождения")
    dateofdeath = models.DateField(null=True, blank=True, verbose_name="Дата смерти")
    biography = models.TextField(null=True, blank=True, verbose_name="Биография")
    photo = models.ImageField(null=True, blank=True, verbose_name="Фотография")
    is_deleted = models.BooleanField(default=False)

    objects = SoftDeleteManager()

    def __str__(self):
        return self.surname

class Book(models.Model):
    title = models.CharField(max_length=55, verbose_name='Название')
    author = models.ForeignKey(Author, on_delete=models.PROTECT)
    publicationdate = models.DateField()
    file = models.FileField(null=True, blank=True)
    cover = models.ImageField(null=True, blank=True, verbose_name="Обложка")
    description = models.TextField(max_length=2500, null=True, blank=True, verbose_name="Описание")

    def __str__(self):
        return self.title

class Bookmark(models.Model):
    bookmark_id = models.AutoField(primary_key=True)
    user = models.OneToOneField(User, on_delete=models.PROTECT, related_name='bookmarks')
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='bookmarks')

class UserInfo(models.Model):
    user = models.OneToOneField(User, on_delete=models.PROTECT, verbose_name="Пользователь")
    avatar = models.FileField(null=True, blank=True, verbose_name="Аватар")
    phone_number = models.CharField(max_length=15, verbose_name="Номер телефона")
    bookmarks = models.ManyToManyField(Bookmark, blank=True, related_name='bookmarks', verbose_name='Закладки')