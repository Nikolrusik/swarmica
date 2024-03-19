from django.db import models


class Department(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey('Author', on_delete=models.CASCADE)
    year = models.DateField(blank=True)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()

    def __str__(self):
        return self.title


class Visitor(models.Model):
    name = models.CharField(max_length=100)
    borrowed_books = models.ManyToManyField(
        Book, related_name='borrowers', blank=True)

    def __str__(self):
        return self.name


class Author(models.Model):
    name = models.CharField(max_length=100, verbose_name='Full name')
    birthday = models.DateField(verbose_name='Birthday',)

    def __str__(self):
        return f'{self.name} - {self.birthday}'
