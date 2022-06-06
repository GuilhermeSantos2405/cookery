from django.test import TestCase
from recipes.models import Category, Recipe, User


class RecipeMixin:
    def make_category(self, name='Category'):
        return Category.objects.create(name=name)

    def make_author(
        self,
        first_name='user',
        last_name='name',
        username='username',
        password='123456',
        email='username@email.com',
    ):
        return User.objects.create_user(
            first_name=first_name,
            last_name=last_name,
            username=username,
            password=password,
            email=email,
        )

    def make_recipe(
        self,
        category_data=None,
        author_data=None,
        title='Recipe Title',
        preparation_time=10,
        servings=5,
        ingredients='ingredients tests',
        method_preparation='method_preparation test',
        is_published=True,
    ):
        if category_data is None:
            category_data = {}

        if author_data is None:
            author_data = {}

        return Recipe.objects.create(
            category=self.make_category(**category_data),
            author=self.make_author(**author_data),
            title=title,
            preparation_time=preparation_time,
            servings=servings,
            ingredients=ingredients,
            method_preparation=method_preparation,
            is_published=is_published,
        )

    def make_recipe_in_batch(self, qtd=10):
        recipes = []
        for i in range(qtd):
            kwargs = {
                'title': f'Recipe Title {i}',
                'author_data': {'username': f'u{i}'}
            }
            recipe = self.make_recipe(**kwargs)
            recipes.append(recipe)
        return recipes


class TestBase(TestCase, RecipeMixin):

    def setUp(self) -> None:
        return super().setUp()
