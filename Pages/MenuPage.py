from selenium.webdriver.common.by import By

from Config.TestData import TestData
from Pages.BasePage import BasePage
from Pages.LoginPage import LoginPage

class MenuPage(LoginPage):
    account_menu = (By.XPATH,"//a[@title='View my customer account']")


