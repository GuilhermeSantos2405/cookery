import pytest
from selenium.webdriver.common.by import By  # Pegar os dados do site
from selenium.webdriver.common.keys import Keys

from .base import RecipeBaseFunctionalTest

server_name = 'http://127.0.0.1:8000'


@pytest.mark.functional_test
class RecipeHomePageFunctionalTest(RecipeBaseFunctionalTest):

    def test_recipe_home_page_without_recipes_not_found_message(self):
        # Pega o site do servidor automaticamente
        self.browser.get(self.live_server_url)
        body = self.browser.find_element(By.TAG_NAME, 'body')
        self.assertIn('Nenhuma receita encontrada', body.text)

    def test_recipe_search_input_can_find_correct_recipes(self):
        title_needed = 'CARNE'
        self.browser.get(server_name)
        search_input = self.browser.find_element(
            By.XPATH,
            '//input[@placeholder="Buscar receitas"]'
        )
        # Clica neste input e digita o termo de busca
        # para encontrar a receita o título desejado """
        search_input.send_keys(title_needed)
        search_input.send_keys(Keys.ENTER)
        # O usuário vê o que estava procurando na página """
        self.assertIn(
            title_needed,
            self.browser.find_element(By.TAG_NAME, 'body').text,
        )

    def test_recipe_home_page_pagination(self):

        # Usuário abre a página
        self.browser.get(server_name)

        # Vê que tem uma paginação e clica na página 2
        page2 = self.browser.find_element(
            By.XPATH,
            '//*[@id="topo"]/div[3]/ul/li[2]/a'
        )
        page2.click()

        # Vê que tem mais 8 receitas na página 8
        self.assertEqual(
            len(self.browser.find_elements(By.CLASS_NAME, 'recipe')),
            8
        )
