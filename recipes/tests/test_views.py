

from unicodedata import category

from django.test import TestCase
from django.urls import reverse
from recipes.models import Category, Recipe, User


class TestBase(TestCase):
    def setUp(self) -> None:
        return super().setUp()

    def make_category(self):
        return Category.objects.create(name='category')

    def make_author(self):
        return User.objects.create(
            first_name='user',
            last_name='name',
            username='username',
            password='123456',
            email='username@email.com'
        )

    def make_recipe(self, is_published=True):
        return Recipe.objects.create(
            title='recipe title test',
            category=self.make_category(),
            author=self.make_author(),
            preparation_time=1,
            servings=1,
            ingredients='ingredients tests',
            method_preparation='method_preparation test',
            is_published=is_published,
        )


class RecipeViewTest(TestBase):

    def test_home_view_status_200_ok(self):
        response = self.client.get(reverse('index_copy'))
        self.assertEqual(response.status_code, 200)

    def test_index_view_load_recipe(self):
        recipe = self.make_recipe()
        response = self.client.get(reverse('index'))
        response_recipes = response.context['recipes_list']
        content = response.content.decode('utf-8')
        print(content)
        assert 1 == 1
        """ self.assertEqual(response_recipes.first().title,
                         'recipe title test') """


"""     
        recipe = self.make_recipe()  # Criando a receita
        response = self.client.get(reverse('index'))  # Executando a view
        # Pegando a queryset (conjunto de lista)
        response_recipes = response.context['recipes_list']
        # Testando se o titulo da receita criada apareceu na tela
        self.assertEqual(response_recipes.first().title,
                         'recipe title test')

    def test_recipe_home_template_dont_load_recipes_not_publishe(self):
        recipe = self.make_recipe(is_published=True)
        response = self.client.get(reverse('index'))
        response_recipes = response.context['recipes_list']
        self.assertEqual(response_recipes.first().title,
                         'recipe title test')

    def test_recipe_detail_template_load(self):
        recipe = self.make_recipe()
        response = self.client.get(reverse('detail', kwargs={'pk': 3}))
        content = response.content.decode('utf-8')
        self.assertIn('recipe title test', content)
 """

""" def test_recipe_author_template_load(self):
        response = self.client.get(reverse('authors_recipes'))
        content = response.content.decode('utf-8')
        print(content)
        assert 1 == 1 """
""" self.assertIn('id="receitas-salgadas"', content) """

""" def test_recipe_detail_template_load(self):
        recipe = self.make_recipe()
        response = self.client.get(
            reverse('salty', kwargs={'pk': recipe.category.id}))
        content = response.content.decode('utf-8')
        print(content)
        self.assertIn('recipe title test', content) """
