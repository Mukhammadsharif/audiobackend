from django.db import models

# Create your models here.
from core.models import BaseModel
from main.querysets.compositions import CompositionQuerySet


class Author(BaseModel):
    full_name = models.CharField(max_length=255, null=True, blank=True, verbose_name='ФИО')
    username = models.CharField(max_length=255, verbose_name='Имя пользователя')
    email = models.CharField(unique=True, max_length=150, verbose_name='Email')
    phone = models.CharField(max_length=20, null=True, blank=True, verbose_name='Номер телефона')

    def __str__(self):
        return self.full_name

    class Meta:
        verbose_name = 'author'
        verbose_name_plural = 'authors'


class Composition(BaseModel):
    title = models.CharField(max_length=255, verbose_name='Название произвидение')
    author = models.ForeignKey(Author, models.CASCADE, verbose_name='Автор')
    genre = models.CharField(max_length=255, verbose_name='Жанр')
    subscription = models.BooleanField(default=False, verbose_name='Подписка')
    description = models.TextField(verbose_name='Описание')
    audiobook_file = models.FileField(upload_to='audiobooks/composition/audio', null=True, blank=True, verbose_name='Аудио сказки')
    duration_of_audio = models.IntegerField(null=True, blank=True,
                                            verbose_name='Продолжительность сказки (В секундах)')
    size_of_audio = models.FloatField(verbose_name="Размер аудиофайла", default='0.00')
    image_file = models.ImageField(upload_to='audiobooks/composition/images', null=True, blank=True, verbose_name='Обложка сказки')
    published_date = models.CharField(verbose_name="Дата публикации", max_length=150)
    age_limit = models.IntegerField(default='0', verbose_name="Возрастной лимит")
    catalog = models.ForeignKey('main.Catalog', models.CASCADE, verbose_name='Каталог', null=True)

    objects = CompositionQuerySet.as_manager()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'composition'
        verbose_name_plural = 'compositions'


class Liked(BaseModel):
    user = models.ForeignKey('users.User', models.CASCADE)
    composition = models.ForeignKey(Composition, models.CASCADE)

    class Meta:
        verbose_name = 'Liked'
        verbose_name_plural = 'Liked'

    def __str__(self):
        return self.composition.title


class Deferred(BaseModel):
    user = models.ForeignKey('users.User', models.CASCADE)
    composition = models.ForeignKey(Composition, models.CASCADE)

    class Meta:
        verbose_name = 'Deferred'
        verbose_name_plural = 'Deferred'

    def __str__(self):
        return self.composition.title


class Catalog(BaseModel):
    title = models.CharField(max_length=255, verbose_name='Загаловок каталога')
    image = models.ImageField(upload_to='audiobooks/catalog/image', null=True, verbose_name='Обложка катлога')

    class Meta:
        verbose_name = 'Catalog'
        verbose_name_plural = 'Catalogs'

    def __str__(self):
        return self.title
