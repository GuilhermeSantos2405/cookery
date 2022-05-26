
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView

from .forms import Registerform


class AuthorsCreateView(CreateView):
    template_name = 'authors/templates/create_authors.html'
    form_class = Registerform
    success_url = reverse_lazy('index')
