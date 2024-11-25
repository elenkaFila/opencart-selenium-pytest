from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select

import time
from selenium import webdriver
from faker import Faker



# fake = Faker("ru_RU")
# print(fake.name())
# print(fake.first_name())
# print(fake.last_name())
# print(fake.email())
# print(fake.password())

# CURENT_CURRENCY = ('css selector','.dropdown strong')
# CURRENCY_MENU = ("id", "form-currency")
# CURRENCIES = ('css selector','#form-currency li')
# PRODUCT_PRICE_CURRENCY = ('class name', 'price-new')
# PRODUCT_PRICE_TAX_CURRENCY = ('class name', 'price-tax')
BUTTON_CONTINUE = ('id','logo')
driver = webdriver.Chrome()
driver.get("http://localhost/index.php?route=account/register&language=en-gb")

driver.find_element(*BUTTON_CONTINUE).click()
print(driver.title)
# #alert = WebDriverWait(driver, 15, poll_frequency=1).until(EC.alert_is_present())
# alert = driver.switch_to.alert
# alert_text = alert.text
# assert alert_text == "Warning: You must agree to the Privacy Policy!"


# driver.find_element(*CURRENCY_MENU).click()
# all_currencies = driver.find_elements(*CURRENCIES)
# all_currencies_text = [x.text for x in all_currencies]
# for currency in all_currencies_text:
#     driver.find_element('xpath',f'//*[text()="{currency}"]').click()
#     text = currency.split(" ", 1)[0] 
#     print(text)
#     print(driver.find_element(*CURENT_CURRENCY).text)
#     assert text == driver.find_element(*CURENT_CURRENCY).text, 'Не получилось поменять валюту'
    
#     for price_type in (PRODUCT_PRICE_CURRENCY,PRODUCT_PRICE_TAX_CURRENCY):
#         for price_elem in driver.find_elements(*price_type):
#             assert text in price_elem.text, f"В цене {price_elem.text} отсутствует валюта {text}"
#     driver.find_element(*CURRENCY_MENU).click()