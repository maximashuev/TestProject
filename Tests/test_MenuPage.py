import pytest
from Config.TestData import TestData
from Pages.LoginPage import LoginPage
from Pages.MenuPage import MenuPage


@pytest.mark.usefixtures("init_driver")
class TestMenuPage:

    def test_page_title_is_correct(self):
        login_page = LoginPage(self.driver)
        login_page.login(TestData.username, TestData.password)
        assert MenuPage(self.driver).get_title(TestData.account_page_title) == TestData.account_page_title

    def test_url_is_correct(self):
        assert self.driver.current_url == TestData.account_url

    def test_username_on_page(self):
        assert MenuPage(self.driver).get_element_text(MenuPage.ACCOUNT_NAME) == TestData.username_on_page

    def test_menu_items_are_clickable(self):
        for button in MenuPage(self.driver).get_menu_items(MenuPage.MENU_ITEMS):
            print(button.text)
            print(button.is_enabled() and button.is_displayed())
            assert (button.is_enabled() and button.is_displayed()) == True
