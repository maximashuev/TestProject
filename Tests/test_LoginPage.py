import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from Config.TestData import TestData
from Pages.LoginPage import LoginPage


@pytest.mark.usefixtures("init_driver")
class TestLoginPage:

    def test_login_button_is_present(self):
        login_page = LoginPage(self.driver)
        is_visible = login_page.is_visible(login_page.SIGH_IN_BUTTON)

        assert is_visible == True

    def test_login_button_text_as_expected(self):

        assert LoginPage(self.driver).get_element_text(LoginPage.SIGH_IN_BUTTON) == 'Sign in'

    def test_login(self):
        LoginPage(self.driver).login(TestData.username,TestData.password)
