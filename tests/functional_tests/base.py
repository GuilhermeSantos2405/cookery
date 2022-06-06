from django.contrib.staticfiles.testing import \
    StaticLiveServerTestCase  # Para carregar os arquivos estático (porém não se deve usar pela demora/peso)
from recipes.tests.test_testbase import RecipeMixin
from selenium.webdriver.common.by import By
from utils.browser import make_chrome_browser


class RecipeBaseFunctionalTest(StaticLiveServerTestCase, RecipeMixin):
    def setUp(self) -> None:
        self.browser = make_chrome_browser()
        return super().setUp()

    def tearDown(self) -> None:
        self.browser.quit()
        return super().tearDown()

    def get_elemenet_by_XPATH(self, element):
        element_input = self.browser.find_element(
            By.XPATH,
            f'{element}'
        )
        return element_input
