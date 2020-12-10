import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager

browser = 'firefox'
driver = None

if browser == 'chrome':
    options = webdriver.ChromeOptions()
    options.headless =True
    # options.add_argument('--headless')
    driver = webdriver.Chrome(ChromeDriverManager().install(),options=options)
elif browser == 'firefox':
    options = webdriver.FirefoxOptions()
    options.add_argument('--headless')
    driver = webdriver.Firefox(executable_path=GeckoDriverManager().install(),options=options)
else:
    print('вап')
    raise Exception

driver.implicitly_wait(5)

driver.get('https://google.com')
print(driver.title)

search_field = driver.find_element(By.NAME,'q')
search_field.send_keys('selenium')

option_list = driver.find_elements(By.CSS_SELECTOR,'ul.erkvQe li span')
print(len(option_list))

for element in option_list:
    print(element.text)

    if element.text == 'selenium foods':
        element.click()
        break

time.sleep(3)
driver.quit()