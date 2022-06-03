
from unicodedata import category

from django.test import TestCase
from django.urls import reverse


class RecipeUTLsTest(TestCase):
    def test_recipe_home_url_is_correct(self):
        home_url = reverse('index')
        self.assertEqual('/', home_url)

    def test_recipe_category_url_is_correct(self):
        category_url = reverse('category', kwargs={'category_id': 1})
        self.assertEqual('/category/1', category_url)

    def test_recipe_detail_url_is_correct(self):
        detail_url = reverse('detail', kwargs={'pk': 1})
        self.assertEqual('/detail/1', detail_url)

    def test_recipe_recipe_create_url_is_correct(self):
        recipe_create_url = reverse('recipe_create')
        self.assertEqual('/recipe_create', recipe_create_url)

    def test_recipe_search_url_is_correct(self):
        search_url = reverse('search')
        self.assertEqual('/search', search_url)
