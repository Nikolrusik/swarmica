from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action
from apps.library.models import Department, Book, Visitor
from apps.library.filters import BookFilter
from apps.library import serializers
from drf_spectacular.utils import extend_schema


class DepartmentViewSet(viewsets.ModelViewSet):
    queryset = Department.objects.all()
    serializer_class = serializers.DepartmentSerializer


class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = serializers.BookSerializer
    search_fields = ('author', 'title',)
    filterset_class = BookFilter

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return serializers.BookGetSerializer
        return serializers.BookSerializer


class VisitorViewSet(viewsets.ModelViewSet):
    queryset = Visitor.objects.all()
    serializer_class = serializers.VisitorSerializer
    search_fields = ('name', )

    def get_serializer_class(self):
        serializer = super().get_serializer_class()
        if self.request.method == 'GET':
            if self.action == 'list':
                serializer = serializers.VisitorListSerializer
            if self.action == 'retrieve':
                serializer = serializers.VisitorRetrieveSerializer

        return serializer

    @extend_schema(request=serializers.VisitorBorrowBooksSerializer)
    @action(detail=True, methods=['post'])
    def borrow_book(self, request, pk=None):
        visitor = self.get_object()
        serializer = serializers.VisitorBorrowBooksSerializer(
            data=request.data)

        if serializer.is_valid(raise_exception=True):
            book = serializer.validated_data.get('book')
            book.quantity -= 1
            book.save()
            visitor.borrowed_books.add(book)
            visitor.save()

            return Response({'success': f'Books {book} borrowed by {visitor.name}'}, status=status.HTTP_200_OK)

    @extend_schema(request=serializers.VisitorReturnBooksSerializer)
    @action(detail=True, methods=['post'])
    def return_book(self, request, pk=None):
        visitor = self.get_object()
        serializer = serializers.VisitorReturnBooksSerializer(
            data=request.data,
            context={'visitor': visitor})

        if serializer.is_valid(raise_exception=True):
            book = serializer.validated_data.get('book')
            book.quantity += 1
            book.save()
            visitor.borrowed_books.remove(book)

            return Response({'success': f'Books "{book}" returned by {visitor.name}'}, status=status.HTTP_200_OK)
