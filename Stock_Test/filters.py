from .models import Stock
import django_filters


class StockFilter(django_filters.rest_framework.FilterSet):
    """
    Stock filter by date and code
    """
    start_date = django_filters.DateFilter(field_name="date", lookup_expr='gte')
    end_date = django_filters.DateFilter(field_name="date", lookup_expr='lte')
    code = django_filters.CharFilter(field_name='code')

    class Meta:
        model = Stock
        fields = ['start_date', 'end_date']