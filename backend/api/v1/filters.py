from django.contrib.auth import get_user_model
from django_filters.rest_framework import FilterSet, filters

from recipes.models import Ingredient, Recipe

User = get_user_model()


class IngredientFilter(FilterSet):
    """Filter for searching ingredients by name."""

    name = filters.CharFilter(lookup_expr='istartswith')

    class Meta:
        model = Ingredient
        fields = ['name']


class RecipeFilter(FilterSet):
    """Filter for searching recipes by author, tags.
    Also filters recipes by is_favorited and is_in_shopping_cart.
    """

    tags = filters.AllValuesMultipleFilter(field_name='tags__slug')
    is_favorited = filters.BooleanFilter(method='filter_is_favorited')
    is_in_shopping_cart = filters.BooleanFilter(
        method='filter_is_in_shopping_cart'
    )

    class Meta:
        model = Recipe
        fields = ['author', 'tags']

    def filter_is_favorited(self, queryset, _, value):
        user = self.request.user
        if value and user.is_authenticated:
            return queryset.filter(favorites__id=user.id)
        return queryset

    def filter_is_in_shopping_cart(self, queryset, _, value):
        user = self.request.user
        if value and user.is_authenticated:
            return queryset.filter(shopping_cart__id=user.id)
        return queryset
