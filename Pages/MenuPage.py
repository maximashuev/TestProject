from selenium.webdriver.common.by import By

from Pages.BasePage import BasePage


class MenuPage(BasePage):
    ACCOUNT_NAME = (By.XPATH, "//a[@title='View my customer account']")
    HEADER = (By.CSS_SELECTOR, "h1.page-heading")
    MENU_ITEMS = (By.XPATH, "//div[@class='row addresses-lists']//a")


    def __init__(self, driver):
        super().__init__(driver)
        self.menu_urls = {}

    def collect_menu_items_in_dic(self):
        for item in BasePage(self.driver).get_menu_items(MenuPage.MENU_ITEMS):
            self.menu_urls.update({item.text:item.get_attribute('href')})
        return self.menu_urls

