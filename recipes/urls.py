from django.urls import path

from .views import (DessertListView, DrinksListView, IndexTemplateView,
                    RecipeCreateView, RecipeDetailView, SaltyListView,
                    SearchListView)

urlpatterns = [
    path('', IndexTemplateView.as_view(), name='index'),
    path('salty', SaltyListView.as_view(), name='salty'),
    path('drinks', DrinksListView.as_view(), name='drinks'),
    path('dessert', DessertListView.as_view(), name='dessert'),
    path('detail/<int:pk>', RecipeDetailView.as_view(), name='detail'),
    path('recipe_create', RecipeCreateView.as_view(), name='recipe_create'),
    path('search', SearchListView.as_view(), name='search'),

]
