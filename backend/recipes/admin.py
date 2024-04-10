from django.contrib import admin

from recipes.models import (
    FavoriteRecipes,
    Ingredient,
    IngredientQuantity,
    Recipe,
    ShoppingCart,
    Tag,
)


class IngredientQuantityInline(admin.TabularInline):
    model = IngredientQuantity
    extra = 1


class IngredientAdmin(admin.ModelAdmin):
    inlines = [IngredientQuantityInline]
    list_display = ['name', 'measurement_unit']
    search_fields = ['name']
    list_filter = ['name']
    list_display_links = ['name']


class RecipeAdmin(admin.ModelAdmin):
    inlines = [IngredientQuantityInline]
    list_display = ['name', 'author']
    search_fields = ['name', 'author', 'tags']
    list_filter = ['author', 'name', 'tags']
    list_display_links = ['name']


admin.site.register(Ingredient, IngredientAdmin)
admin.site.register(Recipe, RecipeAdmin)
admin.site.register(Tag)
admin.site.register(FavoriteRecipes)
admin.site.register(ShoppingCart)
