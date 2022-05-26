from django.urls import reverse_lazy
from django.views.generic import DetailView, ListView

from .models import Recipe


class IndexTemplateView(ListView):
    template_name = 'pages/index.html'
    context_object_name = 'recipes_list'
    model = Recipe
    recipe = Recipe.objects.all()


class RecipeDetailView(DetailView):
    template_name = 'pages/recipe_detail.html'
    login_url = reverse_lazy('login')
    model = Recipe
