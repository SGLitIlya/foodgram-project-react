from django.urls import include, path
from rest_framework.routers import DefaultRouter

from api.v1.views import (
    IngredientViewSet,
    RecipeViewSet,
    TagViewSet,
    UserModelViewSet,
)

v1_router = DefaultRouter()
v1_router.register('ingredients', IngredientViewSet, basename='ingredient')
v1_router.register('tags', TagViewSet, basename='tag')
v1_router.register('recipes', RecipeViewSet, basename='recipe')
v1_router.register('users', UserModelViewSet, basename='user')

urlpatterns = [
    path('', include(v1_router.urls)),
    path('auth/', include('djoser.urls.authtoken')),
]
