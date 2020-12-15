import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager


@pytest.fixture(params=['chrome','firefox'], scope='class')
def init_driver(request):
    driver = None
    if request.param == 'chrome':
        options = webdriver.ChromeOptions()
        # options.headless = True
        options.add_argument('--headless')
        driver = webdriver.Chrome(ChromeDriverManager().install(),options=options)
        driver.implicitly_wait(5)

    elif request.param == 'firefox':
        options = webdriver.FirefoxOptions()
        options.add_argument('--headless')
        driver = webdriver.Firefox(executable_path=GeckoDriverManager().install(),options=options)
        driver.implicitly_wait(5)


    request.cls.driver = driver
    yield
    driver.quit()