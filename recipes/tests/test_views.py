
from django.urls import reverse

from .test_testbase import TestBase


class Recipe(TestBase):

    def test_recipe_index_view_returns_status_code_200_OK(self):
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)

    def test_recipe_index_template_loads_recipes(self):
        # Need a recipe for this test
        self.make_recipe()
        response = self.client.get(reverse('index'))
        response_context_recipes = response.context['recipes_list'].first(
        ).title
        # Check if one recipe exists
        self.assertEqual('Recipe Title', response_context_recipes)

    def test_recipe_index_template_do_not_loads_recipes(self):
        response = self.client.get(reverse('index'))
        content = response.content.decode('utf-8')
        self.assertIn('Nenhuma receita encontrada', content)

    def test_recipe_index_template_dont_load_recipes_not_published(self):
        self.make_recipe(is_published=False)
        response = self.client.get(reverse('index'))
        content = response.content.decode('utf-8')
        self.assertIn('Nenhuma receita encontrada', content)

    def test_recipe_index_template_load_recipes_is_published(self):
        self.make_recipe(is_published=True)
        response = self.client.get(reverse('index'))
        response_context_recipes = response.context['recipes_list'].first(
        ).title
        self.assertEqual('Recipe Title', response_context_recipes)

    def test_category_view_template_load_recipes(self):
        recipe = self.make_recipe()
        response = self.client.get(
            reverse('category', args=(recipe.id,)))
        content = response.content.decode('utf-8')
        self.assertIn('RECIPE TITLE', content)

    def test_category_view_template_do_not_loads_recipes(self):
        recipe = self.make_recipe()
        response = self.client.get(
            reverse('category', args=(recipe.category_id + 1000,)))
        content = response.content.decode('utf-8')
        self.assertIn('Nenhuma receita encontrada', content)

    def test_category_view_template_do_not_loads_is_published_false(self):
        recipe = self.make_recipe(is_published=False)
        response = self.client.get(
            reverse('category', args=(recipe.category_id,)))
        content = response.content.decode('utf-8')
        self.assertIn('Nenhuma receita encontrada', content)

    def test_detail_view_template_load_recipes(self):
        recipe = self.make_recipe()
        response = self.client.get(
            reverse('detail', args=(recipe.id,)))
        content = response.content.decode('utf-8')
        self.assertIn('Recipe Title', content)

    def test_detail_view_template_do_not_load_recipes(self):
        recipe = self.make_recipe()
        response = self.client.get(
            reverse('detail', args=(recipe.id+1000,)))
        status_code = response.status_code
        self.assertEqual(status_code, 404)
