from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

from Pages.LoginPage import LoginPage


class Test_LoginPage:

    def test_login_button_is_present(self):
        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.implicitly_wait(5)

        login_page = LoginPage(driver)
        is_visible = login_page.is_visible(login_page.sing_in_button)

        assert is_visible == True
