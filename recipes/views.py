from django.views.generic import ListView, TemplateView

from .models import Recipe


class IndexTemplateView(ListView):
    template_name = 'pages/index.html'
    context_object_name = 'recipes_list'
    model = Recipe
    recipe = Recipe.objects.all()
