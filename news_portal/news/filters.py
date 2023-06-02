import django_filters
from django_filters import FilterSet, ModelChoiceFilter, ModelMultipleChoiceFilter
from .models import Post, Category, Author, User, PostCategory
from django import forms


class NewsFilter(FilterSet):
    date = django_filters.DateFilter(field_name="datetime_create", widget=forms.DateInput(attrs={'type': "date"}),
                                     label='Дата', lookup_expr='date__gte')
    category = ModelChoiceFilter(
        field_name='postcategory__id_category',
        queryset=Category.objects.all(),
        label='Категория',
        empty_label ='Все',
    )
    # author = ModelChoiceFilter(
    #     field_name='post__id_author',
    #     qyeryset = Author.id_user(),
    #     label='Автор',
    #     empty_label='Все',
    # )

    class Meta:
       model = Post
       fields = {
           #'postcategory__id_category':['in'],
           'article':['icontains'],
           'state_news':['exact'],
           #'id_author':['in'],
           #'id_cat':['exact'],



       }