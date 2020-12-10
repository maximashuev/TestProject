from selenium.webdriver.common.by import By

from Config.TestData import TestData
from Pages.BasePage import BasePage


class LoginPage(BasePage):
    username_field = (By.NAME, "login_email")
    password_field = (By.NAME, "login_email")
    sing_in_button = (By.XPATH, "/html//div[@id='login-or-register-page-content']/div/div/div[@class='login-register-login-part']/div[2]/div//form[@method='POST']//div[@class='signin-text']")
    account_menu = (By.XPATH,"//span[contains(text(),'HA')]")

    def __init__(self,driver):
        super().__init__(driver)
        self.driver.get(TestData.BASE_URL)

    def login(self, username, password):
        self.send_keys(self.username_field,username)
        self.send_keys(self.password_field,password)
        self.click(self.sing_in_button)
        self.is_visible(self.username_text)