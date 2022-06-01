from django.test import TestCase
from model_mommy import mommy


class CategoryTestCase(TestCase):
    # criando arquivo para comparar
    def setUp(self):
        self.category = mommy.make('Category')

    # Comparação
    def test_str(self):
        self.assertEquals(str(self.category), self.category.name)


class RecipeTestCase(TestCase):
    def setUp(self):
        self.recipe = mommy.make('Recipe')

    def test_str(self):
        self.assertEquals(str(self.recipe), self.recipe.title)
