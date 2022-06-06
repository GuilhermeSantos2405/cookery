from time import sleep

from selenium.webdriver.common.by import By  # Pegar os dados do site
from selenium.webdriver.common.keys import Keys

from .base import RecipeBaseFunctionalTest

server_name = 'http://127.0.0.1:8000'


class AuthorsRegisterTest(RecipeBaseFunctionalTest):

    def get_elemenet_by_XPATH(self, element):
        element_input = self.browser.find_element(
            By.XPATH,
            f'{element}'
        )
        return element_input

    def test_user_name_register_form(self):
        self.browser.get(self.live_server_url + '/authors/create')

        user_name_input = self.get_elemenet_by_XPATH('//*[@id="id_username"]')
        # Preenchendo todos os campos
        fields = self.browser.find_elements(By.TAG_NAME, 'input')
        for field in fields:
            if field.is_displayed():
                field.send_keys(' ' * 10)
        self.browser.find_element(
            By.NAME, 'email').send_keys('teste@email.com')
        user_name_input.send_keys(Keys.ENTER)

        self.assertIn(
            'Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', self.get_elemenet_by_XPATH('//*[@id="div_id_username"]').text)

    def test_passwords_do_not_match(self):
        self.browser.get(self.live_server_url + '/authors/create')
        password_input_1 = self.get_elemenet_by_XPATH(
            '//*[@id="id_password1"]')
        password_input_2 = self.get_elemenet_by_XPATH(
            '//*[@id="id_password2"]')
        self.browser.find_element(
            By.NAME, 'username').send_keys('user_name_test')
        self.browser.find_element(
            By.NAME, 'email').send_keys('teste@email.com')
        password_input_1.send_keys('P@ssw0rd')
        password_input_2.send_keys('P@ssw0rd_diferent')
        password_input_2.send_keys(Keys.ENTER)

        self.assertIn('two password fields didn’t match.', self.get_elemenet_by_XPATH(
            '//*[@id="div_id_password2"]').text)

    def test_user_valid_data_register_successfully(self):
        self.browser.get(self.live_server_url + '/authors/create')
        self.get_elemenet_by_XPATH(
            '//*[@id="id_first_name"]').send_keys('First name test')
        self.get_elemenet_by_XPATH(
            '//*[@id="id_last_name"]').send_keys('Last name test')
        self.get_elemenet_by_XPATH(
            '//*[@id="id_email"]').send_keys('test@email.com')
        self.get_elemenet_by_XPATH(
            '//*[@id="id_username"]').send_keys('User_name_test')
        self.get_elemenet_by_XPATH(
            '//*[@id="id_password1"]').send_keys('P@ssw0rd_test_1')
        self.get_elemenet_by_XPATH(
            '//*[@id="id_password2"]').send_keys('P@ssw0rd_test_1')

        self.get_elemenet_by_XPATH(
            '/html/body/form/button').send_keys(Keys.ENTER)
        login = self.browser.find_element(
            By.XPATH,
            '/html/body'
        ).text
        self.assertIn('Login', login)
