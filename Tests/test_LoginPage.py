import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

from Pages.LoginPage import LoginPage


@pytest.mark.usefixtures("init_driver")
class TestLoginPage:

    def test_login_button_is_present(self):
        # options = webdriver.ChromeOptions()
        # options.headless = True
        # # options.add_argument('--headless')
        # driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
        # self.driver.implicitly_wait(5)

        login_page = LoginPage(self.driver)
        is_visible = login_page.is_visible(login_page.sing_in_button)

        assert is_visible == True

    def test_login_button_text_as_expected(self):
        # options = webdriver.ChromeOptions()
        # options.headless = True
        # # options.add_argument('--headless')
        # driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
        # driver.implicitly_wait(5)

        assert LoginPage(self.driver).get_element_text(LoginPage.sing_in_button) == 'Sign in'

    # def test_login_successfully(self):
    #
    #     LoginPage(self.driver).login(LoginPage.username, LoginPage.password)
