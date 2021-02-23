import django_filters
from .models import Problems


class ProductFilter(django_filters.FilterSet):
    Easy = 'Easy'
    Medium = 'Medium'
    Hard = 'Hard'
    NA = 'NA'
    DIFFICULTY = [
        (NA, 'NA'),
        (Easy, 'Easy'),
        (Medium, 'Medium'),
        (Hard, 'Hard'),
    ]

    name_pr = django_filters.CharFilter(field_name='name_problem', lookup_expr='icontains')
    diff = django_filters.ChoiceFilter(field_name='difficulty' ,choices=DIFFICULTY, empty_label='Difficulty')

    class Meta:
        model = Problems
        fields = ['name_pr', 'diff']