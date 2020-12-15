import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

from Pages.LoginPage import LoginPage


@pytest.mark.usefixtures("init_driver")
class TestLoginPage:

    def test_login_button_is_present(self):

        login_page = LoginPage(self.driver)
        is_visible = login_page.is_visible(login_page.sing_in_button)

        assert is_visible == True

    def test_login_button_text_as_expected(self):

        assert LoginPage(self.driver).get_element_text(LoginPage.sing_in_button) == 'Sign in with Google'

    def test_login_button_clickable(self):
        LoginPage(self.driver).login(LoginPage.username,LoginPage.password)
