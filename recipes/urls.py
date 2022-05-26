from django.urls import path

from .views import IndexTemplateView, RecipeCreateView, RecipeDetailView

urlpatterns = [
    path('', IndexTemplateView.as_view(), name='index'),
    path('detail/<int:pk>', RecipeDetailView.as_view(), name='detail'),
    path('recipe_create', RecipeCreateView.as_view(), name='recipe_create'),

]
