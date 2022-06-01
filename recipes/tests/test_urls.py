
from django.test import TestCase
from django.urls import reverse


class RecipeUTLsTest(TestCase):
    def test_recipe_home_url_is_correct(self):
        home_url = reverse('index')
        self.assertEqual('/', home_url)

    def test_recipe_salty_url_is_correct(self):
        salty_url = reverse('salty')
        self.assertEqual('/salty', salty_url)

    def test_recipe_drinks_url_is_correct(self):
        drinks_url = reverse('drinks')
        self.assertEqual('/drinks', drinks_url)

    def test_recipe_dessert_url_is_correct(self):
        dessert_url = reverse('dessert')
        self.assertEqual('/dessert', dessert_url)

    def test_recipe_search_url_is_correct(self):
        search_url = reverse('search')
        self.assertEqual('/search', search_url)

    def test_recipe_recipe_create_url_is_correct(self):
        recipe_create_url = reverse('recipe_create')
        self.assertEqual('/recipe_create', recipe_create_url)

    def test_recipe_detail_url_is_correct(self):
        detail_url = reverse('detail', kwargs={'pk': 1})
        self.assertEqual('/detail/1', detail_url)
