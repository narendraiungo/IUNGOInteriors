from .models import sub_category, Client, FeedbackRating
import django_filters


class SubcategoryForm(django_filters.filterset):
    class Meta:
        model = sub_category
        fields = ['name', 'category']


choices=(('low-high','Low-High'),('high-low','High-Low'))

class BudgetFilterForm(django_filters.filterset):
    #budget=Rangefilter()
    class Meta:
        model=Client
        fields=['budget']


class ExperienceFilter(django_filters.filterset):
    class Meta:
        model=Client
        fields=['experience']


class RatingFilterForm(django_filters.filterset):
    class Meta:
        model = FeedbackRating
        fields = ['ratings']
