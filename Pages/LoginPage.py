from selenium.webdriver.common.by import By

from Config.TestData import TestData
from Pages.BasePage import BasePage


class LoginPage(BasePage,TestData):
    username_field = (By.ID, "email")
    password_field = (By.NAME, "passwd")
    sing_in_button = (By.XPATH, "//button[@id='SubmitLogin']/span")
    account_menu = (By.XPATH,"//a[@title='View my customer account']")

    def __init__(self,driver):
        super().__init__(driver)
        self.driver.get(TestData.BASE_URL)

    def login(self, username, password):
            self.send_keys(self.username_field,username)
            self.send_keys(self.password_field,password)
            self.click(self.sing_in_button)
            return self.is_visible(self.account_menu)
