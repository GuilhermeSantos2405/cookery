from time import sleep

from django.contrib.auth.models import User
from selenium.webdriver.common.by import By  # Pegar os dados do site
from selenium.webdriver.common.keys import Keys

from .base import RecipeBaseFunctionalTest


class AuthorsLoginTest(RecipeBaseFunctionalTest):
    def test_recipe_home_page_pagination(self):
        user = User.objects.create_user(
            username='username', password='Pas213172')
        # Usuário abre a página
        self.browser.get(self.live_server_url + '/authors/login/')
        self.get_elemenet_by_XPATH(
            '//*[@id="id_username"]').send_keys('username')
        self.get_elemenet_by_XPATH(
            '//*[@id="id_password"]').send_keys('Pas213172')
        self.get_elemenet_by_XPATH(
            '/html/body/form/button').send_keys(Keys.ENTER)
        username = self.browser.find_element(
            By.XPATH,
            '/html/body'
        ).text
        sleep(5)
        self.assertIn('USERNAME', username)
