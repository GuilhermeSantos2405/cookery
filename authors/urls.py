from django.contrib.auth import views as auth_views
from django.urls import path

from .views import AuthorsCreateView

urlpatterns = [
    path('create', AuthorsCreateView.as_view(), name='create_author'),
    path('login/', auth_views.LoginView.as_view(
         template_name='authors/templates/login.html'
         ), name='login', ),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]
