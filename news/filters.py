from datetime import datetime, date

from django.forms import DateInput
from django_filters import FilterSet, DateFilter, CharFilter
from .models import News

# class NewsFilter(FilterSet):
#     class Meta:
#         model = News
#         fields = {
#             'name': ['icontains'],
#             'description': ['icontains'],
#             'publish_date': ['month__gte'],
#         }

#organizing the search later than certain day

class NewNewsFilter(FilterSet):
    name = CharFilter(lookup_expr='icontains')
    publish_date = DateFilter(
        lookup_expr='gte',
        label='From date on',
        widget=DateInput(
            attrs={
                'type': 'date',
            }
        ),
    )


    class Meta:
        model = News
        fields = {'name', 'publish_date'}



