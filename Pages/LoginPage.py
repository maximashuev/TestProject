from selenium.webdriver.common.by import By

from Config.TestData import TestData
from Pages.BasePage import BasePage


class LoginPage(BasePage):
    USERNAME_FIELD = (By.ID, "email")
    PASSWORD_FIELD = (By.NAME, "passwd")
    SIGH_IN_BUTTON = (By.XPATH, "//button[@id='SubmitLogin']/span")

    def __init__(self,driver):
        super().__init__(driver)
        self.driver.get(TestData.BASE_URL)

    def login(self, username, password):
            self.send_keys(self.USERNAME_FIELD, username)
            self.send_keys(self.PASSWORD_FIELD, password)
            self.click(self.SIGH_IN_BUTTON)
