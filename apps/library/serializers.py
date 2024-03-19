from rest_framework import serializers
from apps.library.models import Department, Book, Visitor
from rest_framework.exceptions import ValidationError


class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = '__all__'


class BookGetSerializer(serializers.ModelSerializer):
    department = serializers.StringRelatedField()
    author = serializers.StringRelatedField()

    class Meta:
        model = Book
        fields = '__all__'


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'


class VisitorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Visitor
        fields = "__all__"


class VisitorListSerializer(serializers.ModelSerializer):
    borrowed_books_count = serializers.SerializerMethodField()

    class Meta:
        model = Visitor
        exclude = ('borrowed_books',)

    def get_borrowed_books_count(self, obj):
        return obj.borrowed_books.count()


class VisitorRetrieveSerializer(serializers.ModelSerializer):
    borrowed_books = BookSerializer(many=True)

    class Meta:
        model = Visitor
        fields = "__all__"


class VisitorBorrowBooksSerializer(serializers.Serializer):
    book = serializers.PrimaryKeyRelatedField(queryset=Book.objects.all())

    def validate(self, attrs):
        book = attrs.get('book')

        if book.quantity < 1:
            raise ValidationError({'book': 'Book is not available!'})
        return super().validate(attrs)


class VisitorReturnBooksSerializer(serializers.Serializer):
    book = serializers.PrimaryKeyRelatedField(queryset=Book.objects.all())

    def validate(self, attrs):
        book = attrs.get('book')
        visitor = self.context['visitor']

        if book not in visitor.borrowed_books.all():
            raise ValidationError({'book': 'User don`t have this book!'})

        return super().validate(attrs)
