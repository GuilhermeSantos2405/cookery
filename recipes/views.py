from unicodedata import category

from django.contrib.auth.mixins import LoginRequiredMixin as LRM
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, ListView

from .forms import RecipeRegisterView
from .models import Recipe


class IndexTemplateView(ListView):
    template_name = 'pages/index.html'
    context_object_name = 'recipes_list'
    model = Recipe
    paginate_by = 8

    def get_queryset(self):
        return Recipe.objects.filter(is_published=True).order_by('?')


class SaltyListView(ListView):
    template_name = 'pages/salty.html'
    context_object_name = 'recipes_list'
    model = Recipe
    paginate_by = 6

    def get_queryset(self):
        return Recipe.objects.filter(is_published=True, category_id=1)


class DessertListView(ListView):
    template_name = 'pages/dessert.html'
    context_object_name = 'recipes_list'
    model = Recipe
    paginate_by = 6

    def get_queryset(self):
        return Recipe.objects.filter(is_published=True, category=2)


class DrinksListView(ListView):
    template_name = 'pages/drinks.html'
    context_object_name = 'recipes_list'
    model = Recipe
    paginate_by = 6

    def get_queryset(self):
        return Recipe.objects.filter(is_published=True, category=3)


class RecipeDetailView(DetailView):
    template_name = 'pages/recipe_detail.html'
    login_url = reverse_lazy('login')
    model = Recipe


class RecipeCreateView(LRM, CreateView):
    login_url = reverse_lazy('login')
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
