from django.contrib.auth import views as auth_views
from django.urls import path

from .views import (AuthorRecipesView, AuthorsCreateView, AuthorsDeleteView,
                    AuthorsUpdateView)

urlpatterns = [
    path('create', AuthorsCreateView.as_view(), name='create_author'),
    path('authors_recipes', AuthorRecipesView.as_view(), name='authors_recipes'),
    path('delete_recipe/<int:pk>', AuthorsDeleteView.as_view(), name='delete'),
    path('update_recipe/<int:pk>', AuthorsUpdateView.as_view(), name='update'),
    path('login/', auth_views.LoginView.as_view(
         template_name='authors/templates/login.html'
         ), name='login', ),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]
