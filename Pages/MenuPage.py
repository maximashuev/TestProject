from selenium.webdriver.common.by import By

from Pages.BasePage import BasePage


class MenuPage(BasePage):
    ACCOUNT_NAME = (By.XPATH, "//a[@title='View my customer account']")
    HEADER = (By.CSS_SELECTOR, "h1.page-heading")
    MENU_ITEMS = (By.XPATH, "//div[@class='row addresses-lists']//a")

    def __init__(self, driver):
        super().__init__(driver)

