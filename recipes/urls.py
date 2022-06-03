from django.urls import path

from .views import (CategoryTemplateView, IndexTemplateView, RecipeCreateView,
                    RecipeDetailView, SearchListView)

urlpatterns = [
    path('', IndexTemplateView.as_view(), name='index'),
    path('category/<int:category_id>',
         CategoryTemplateView.as_view(), name='category'),
    path('detail/<int:pk>', RecipeDetailView.as_view(), name='detail'),
    path('recipe_create', RecipeCreateView.as_view(), name='recipe_create'),
    path('search', SearchListView.as_view(), name='search'),

]
