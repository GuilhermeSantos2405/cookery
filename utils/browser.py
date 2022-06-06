from pathlib import Path

from selenium import webdriver
from selenium.webdriver.chrome.service import Service

# Buscar o caminho até a página raiz do projeto (cookety)
ROOT_PATH = Path(__file__).parent.parent
# arquivo baixado feito pelo selenium na pasta bin
CHROMEDRIVER_NAME = 'chromedriver.exe'
CHROMEDRIVER_PATH = ROOT_PATH / 'bin' / CHROMEDRIVER_NAME  # Caminho


def make_chrome_browser(*options):
    chrome_options = webdriver.ChromeOptions()
    # if do  --headless Opcional para caso não queira que abra o browser
    if options is not None:
        for option in options:
            chrome_options.add_argument(option)

    chrome_service = Service(executable_path=CHROMEDRIVER_PATH)
    browser = webdriver.Chrome(service=chrome_service, options=chrome_options)
    return browser


if __name__ == '__main__':
    # --headless Opcional para caso não queira que abra o browser
    browser = make_chrome_browser('--headless')
    browser.get('http://www.google.com/')
    browser.quit()
