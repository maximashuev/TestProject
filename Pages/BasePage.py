from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, driver, timeout=10):
        self.driver = driver
        self.timeout = timeout

    def click(self, by_locator):
        condition = EC.visibility_of_element_located(by_locator)
        element = WebDriverWait(self.driver, self.timeout).until(condition)
        element.click()

    def send_keys(self, by_locator, value):
        condition = EC.visibility_of_element_located(by_locator)
        element = WebDriverWait(self.driver, self.timeout).until(condition)
        element.send_keys(value)

    def get_element_text(self, by_locator):
        condition = EC.visibility_of_element_located(by_locator)
        element = WebDriverWait(self.driver, self.timeout).until(condition)
        return element.text

    def is_visible(self, by_locator):
        condition = EC.visibility_of_element_located(by_locator)
        element = WebDriverWait(self.driver, self.timeout).until(condition)
        return bool(element)

    def get_title(self, title):
        condition = EC.title_is(title)
        WebDriverWait(self.driver, self.timeout).until(condition)
        return self.driver.title

    def get_menu_items(self, by_locator):
        condition = EC.visibility_of_all_elements_located(by_locator)
        menu_items_list= WebDriverWait(self.driver, self.timeout).until(condition)

        return menu_items_list

