from django.db import models


class Department(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Отдел'
        verbose_name_plural = 'Отделы'


class Book(models.Model):
    title = models.CharField(max_length=200, verbose_name='Название')
    author = models.ForeignKey(
        'Author', on_delete=models.CASCADE, verbose_name='Автор')
    year = models.CharField(verbose_name='Год издания')
    department = models.ForeignKey(
        Department, on_delete=models.CASCADE, verbose_name='Отдел')
    quantity = models.PositiveIntegerField(verbose_name='Количество')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Книга'
        verbose_name_plural = 'Книги'


class Visitor(models.Model):
    name = models.CharField(max_length=100, verbose_name='Имя')
    borrowed_books = models.ManyToManyField(
        Book, related_name='borrowers', blank=True, verbose_name='Взятые книги')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Клиент'
        verbose_name_plural = 'Клиенты'


class Author(models.Model):
    name = models.CharField(max_length=100, verbose_name='ФИО')
    birthday = models.DateField(verbose_name='Дата рождения')

    def __str__(self):
        return f'{self.name} - {self.birthday}'

    class Meta:
        verbose_name = 'Автор'
        verbose_name_plural = 'Авторы'

    def __str__(self):
        return f'{self.name} - {self.birthday}'
