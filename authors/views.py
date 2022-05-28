
from django.urls import reverse_lazy
from django.views.generic import DeleteView, ListView, UpdateView
from django.views.generic.edit import CreateView
from recipes.models import Recipe

from .forms import Registerform


class AuthorsCreateView(CreateView):
    template_name = 'authors/templates/create_authors.html'
    form_class = Registerform
    success_url = reverse_lazy('index')


class AuthorRecipesView(ListView):
    template_name = 'authors/templates/authors_recipes.html'
    context_object_name = 'authors_recipes'
    model = Recipe
    paginate_by = 4

    def get_queryset(self):
        return Recipe.objects.filter(author=self.request.user)


class AuthorsDeleteView(DeleteView):
    model = Recipe
    template_name = 'authors/templates/delete_recipe.html'
    success_url = reverse_lazy('index')


class AuthorsUpdateView(UpdateView):
    model = Recipe
    fields = ['title', 'preparation_time', 'servings', 'ingredients',
              'method_preparation', 'image', 'category']
    template_name = 'authors/templates/update_recipe.html'
    success_url = reverse_lazy('index')
