import pytest
from Pages.MenuPage import MenuPage


@pytest.mark.usefixtures("init_driver")
class TestMenuPage:

    def test_page_title_is_correct(self):
        MenuPage(self.driver).login(MenuPage.username,MenuPage.password)
        assert self.driver.title == MenuPage.account_page_title

    def test_url_is_correct(self):
        assert self.driver.current_url == MenuPage.account_url

    def test_username_on_page(self):
        assert MenuPage(self.driver).get_element_text(MenuPage.account_menu) == MenuPage.username_on_page
