from django.urls import path

from .views import IndexTemplateView, RecipeDetailView

urlpatterns = [
    path('', IndexTemplateView.as_view(), name='index'),
    path('detail/<int:pk>', RecipeDetailView.as_view(), name='detail'),

]
