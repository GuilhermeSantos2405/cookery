from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, ListView

from .forms import RecipeRegisterView
from .models import Recipe


class IndexTemplateView(ListView):
    template_name = 'pages/index.html'
    context_object_name = 'recipes_list'
    model = Recipe

    def get_queryset(self):
        return Recipe.objects.filter(is_published=True)


class RecipeDetailView(DetailView):
    template_name = 'pages/recipe_detail.html'
    login_url = reverse_lazy('login')
    model = Recipe


class RecipeCreateView(CreateView):
    model = Recipe
    template_name = 'pages/create_recipe.html'
    form_class = RecipeRegisterView
    success_url = reverse_lazy('index')

    def form_valid(self, form=RecipeRegisterView):
        form.instance.author = self.request.user
        url = super().form_valid(form)
        return url


class SearchListView(ListView):
    template_name = 'pages/search.html'
    context_object_name = 'recipes_list'
    model = Recipe

    def get_queryset(self):
        search_term = self.request.GET.get('search_term')
        qs = Recipe.objects.filter(
            title__icontains=search_term, is_published=True)
        return qs
