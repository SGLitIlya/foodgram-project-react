from colorfield.fields import ColorField
from django.contrib.auth import get_user_model
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models

from core import constants

User = get_user_model()


class Tag(models.Model):
    name = models.CharField(
        'Название',
        unique=True,
        max_length=constants.TAG_NAME_MAX_LEN,
    )
    color = ColorField(
        'Цвет',
        unique=True,
        default='#FF0000',
    )
    slug = models.SlugField(
        'Слаг',
        unique=True,
        max_length=constants.TAG_SLUG_MAX_LEN,
    )

    class Meta:
        ordering = ['name']
        verbose_name = 'Тег'
        verbose_name_plural = 'Теги'

    def __str__(self):
        return self.name


class Ingredient(models.Model):
    name = models.CharField('Название', max_length=constants.ING_NAME_MAX_LEN)
    measurement_unit = models.CharField(
        'Единица измерения', max_length=constants.ING_MES_MAX_LEN
    )

    class Meta:
        ordering = ['name']
        verbose_name = 'Ингредиент'
        verbose_name_plural = 'Ингредиенты'
        constraints = [
            models.UniqueConstraint(
                name='%(app_label)s_%(class)s_unique_relationships',
                fields=['name', 'measurement_unit'],
            ),
        ]

    def __str__(self):
        return self.name


class Recipe(models.Model):
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='recipes',
        verbose_name='Автор',
    )
    name = models.CharField(
        'Название',
        max_length=constants.RECIPE_NAME_MAX_LEN,
    )
    text = models.TextField('Описание')
    cooking_time = models.PositiveSmallIntegerField(
        'Время приготовления',
        validators=[
            MinValueValidator(
                constants.RECIPE_CKN_TIME_MIN,
                constants.RECIPE_CKN_TIME_MIN_ERR_MSG,
            ),
            MaxValueValidator(
                constants.RECIPE_CKN_TIME_MAX,
                constants.RECIPE_CKN_TIME_MAX_ERR_MSG,
            ),
        ],
    )
    image = models.ImageField('Изображение', upload_to='api/imgs/')
    tags = models.ManyToManyField(
        Tag,
        related_name='recipes',
        verbose_name='Теги',
    )
    ingredients = models.ManyToManyField(
        Ingredient,
        related_name='recipes',
        verbose_name='Ингредиенты',
        through='IngredientQuantity',
    )
    favorites = models.ManyToManyField(
        User,
        through='FavoriteRecipes',
        related_name='favorites',
        verbose_name='Избранное',
    )
    shopping_cart = models.ManyToManyField(
        User,
        through='ShoppingCart',
        related_name='shopping_cart',
        verbose_name='Корзина покупок',
    )
    created_at = models.DateTimeField('Дата создания', auto_now_add=True)

    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Рецепт'
        verbose_name_plural = 'Рецепты'

    def __str__(self):
        return self.name


class FavoriteRecipes(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='favorited_by'
    )
    recipe = models.ForeignKey(
        Recipe, on_delete=models.CASCADE, related_name='favorite'
    )

    class Meta:
        ordering = ['-recipe']
        verbose_name = 'Избранное'
        verbose_name_plural = 'Избранное'
        constraints = [
            models.UniqueConstraint(
                name='%(app_label)s_%(class)s_unique_relationships',
                fields=['recipe', 'user'],
            ),
        ]

    def __str__(self):
        return f'Рецепт {self.recipe} в избранном у пользователя {self.user}.'


class ShoppingCart(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='shopped_by'
    )
    recipe = models.ForeignKey(
        Recipe, on_delete=models.CASCADE, related_name='shop_cart'
    )

    class Meta:
        ordering = ['-recipe']
        verbose_name = 'Корзина покупок'
        verbose_name_plural = 'Корзины покупок'
        constraints = [
            models.UniqueConstraint(
                name='%(app_label)s_%(class)s_unique_relationships',
                fields=['recipe', 'user'],
            ),
        ]

    def __str__(self):
        return f'Рецепт {self.recipe} в корзине у пользователя {self.user}.'


class IngredientQuantity(models.Model):
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    amount = models.PositiveSmallIntegerField(
        'Количество',
        validators=[
            MinValueValidator(
                constants.ING_AMOUNT_MIN,
                constants.ING_AMOUNT_MIN_ERR_MSG
            ),
            MaxValueValidator(
                constants.ING_AMOUNT_MAX,
                constants.ING_AMOUNT_MAX_ERR_MSG
            ),
        ],
    )

    def __str__(self):
        return (
            f'В рецепте "{self.recipe.__str__()}"'
            f' {self.amount} {self.ingredient.measurement_unit} ингредиента'
            f' {self.ingredient.__str__()}.'
        )
