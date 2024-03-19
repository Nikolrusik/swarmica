from django.contrib import admin
from apps.library.models import Author, Book, Visitor, Department


admin.site.register(Author)
admin.site.register(Book)
admin.site.register(Visitor)
admin.site.register(Department)
