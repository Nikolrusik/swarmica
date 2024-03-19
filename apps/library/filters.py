from django_filters import FilterSet, BooleanFilter
from apps.library.models import Book


class BookFilter(FilterSet):
    is_available = BooleanFilter(
        field_name='quantity', method='filter_is_available')

    class Meta:
        model = Book
        fields = ('author__name', 'year', 'department__name', 'is_available',)

    def filter_is_available(self, queryset, name, value):
        if value:
            queryset.filter(quantity_gt=0)
        return value
