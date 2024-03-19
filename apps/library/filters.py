from django_filters import FilterSet, BooleanFilter
from apps.library.models import Book


class BookFilter(FilterSet):
    is_available = BooleanFilter(
        field_name='quantity', method='filter_is_available')

    class Meta:
        model = Book
        fields = ('author__name', 'year', 'department__name', 'is_available',)

    def filter_is_available(self, queryset, name, value):
        if value is not None:
            if value:
                return queryset.filter(quantity__gt=0)
            return queryset.filter(quantity=0)

        return queryset
