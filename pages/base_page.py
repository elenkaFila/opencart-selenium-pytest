from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support import expected_conditions as EC
import time
import allure

class BasePage:
    """Класс Главной страницы"""
    # картинка 

    LOGO = ("css selector", "#logo a")
    # строка поиска
    SEARCH_BAR = ("class", "form-control")
    # кнопка поиска
    SEARCH_BAR_BUTTON = ("css selector", ".btn[type='submit']")
    # Кнопка перехода в корзину
    CART_BUTTON = ("css selector", ".btn.dropdown-toggle")
    # верхняя навигационная панель
    NAV_TAB = ("css selector", "nav#top")
    # меню валюты
    #CURRENCY_MENU = ("link text", 'Currency')
    CURENT_CURRENCY = ('css selector','.dropdown strong')
    CURRENCY_MENU = ("id", "form-currency")
    CURRENCIES = ('css selector','#form-currency li')
    PRODUCT_PRICE_CURRENCY = ('class name', 'price-new')
    PRODUCT_PRICE_TAX_CURRENCY = ('class name', 'price-tax')
    # меню личного кабинета
    MY_ACCOUNT_MENU = ("xpath", "//li[2]/div/a/span")
    REGISTER_LINK = ("xpath", "//li[2]/div/ul/li[1]")
    WISHLIST_BUTTON = ("id", "wishlist-total")
    SHOPPING_CART_BUTTON = ("css selector", 'a[title="Shopping Cart"]')
    CHECKOUT_BUTTON = ("css selector", 'a[title="Checkout"]')
    # меню сайта
    HEADER_TAB = ("css selector", "nav#menu")
    BUTTON_ADD_TO_CART_PRODUCT = ("css selector",'.col.mb-3:first-child button:nth-child(1)')
    BUTTON_ADD_TO_WISHLIST_PRODUCT = ("css selector",'.col.mb-3:first-child button:nth-child(2)')
    BUTTON_ADD_TO_COMPARE_PRODUCT = ("css selector",'.col.mb-3:first-child button:nth-child(3)')
    ALERT = ('class name', "alert.alert-success.alert-dismissible")


    def __init__(self, driver):
        self.driver: WebDriver = driver
        self.wait = WebDriverWait(driver, 15, poll_frequency=1)
        
    @allure.step('Open page')
    def open(self):
        self.driver.get(self.PAGE_URL)

    def element_get_attribute(self, locator, attribute):
        self.element_is_present(locator)
        return self.driver.find_element(*locator).get_attribute(attribute)

    def is_opened(self):
        self.wait.until(EC.url_to_be(self.PAGE_URL))

    def click_on_element(self, locator):
        self.wait.until(EC.element_to_be_clickable(locator)).click()

    def click_on_invisible_element(self, locator):
        self.wait.until(EC.presence_of_element_located(locator)).click()

    def wait_alert_invisible(self,locator):
        self.wait.until_not(EC.presence_of_element_located(locator))

    def element_is_present(self, locator):
        self.wait.until(EC.presence_of_element_located(locator))
        return True
    
    def element_is_visible(self, locator):
        self.wait.until(EC.visibility_of_element_located(locator))
        return True

    def count_elements(self, locator):
        self.wait.until(EC.presence_of_all_elements_located(locator))
        return len(self.driver.find_elements(*locator))


    def get_text_element(self, locator):
        self.element_is_present(locator)        
        return self.driver.find_element(*locator).text


    def get_text_elements(self, locator):
        list = self.driver.find_elements(*locator)
        return [x.text for x in list]
    
    def enter_text(self, locator, text):
        self.click_on_element(locator)
        self.driver.find_element(*locator).clear()
        self.driver.find_element(*locator).send_keys(text)

    def scroll_to_bottom_page(self, locator):
        height = self.driver.execute_script("return document.body.scrollHeight")
        self.driver.execute_script(f"window.scrollTo(0, {height})")
        self.scroll_to_element(locator)
        time.sleep(1)
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
        
    def scroll_to_element(self, locator):
        self.driver.execute_script("arguments[0].scrollIntoView();", self.driver.find_element(*locator))

    @allure.step("Click on logo page")    
    def click_logo(self):
        self.click_on_element(self.LOGO)
    
    @allure.step("Get title current page")    
    def get_title_page(self):
        return self.driver.title
    
    @allure.step("Get current url")
    def get_current_url(self,url):
        self.wait.until(EC.url_contains(url))
        return self.driver.current_url

    @allure.step("Alert is present")
    def present_alert(self):
        return self.element_is_present(self.ALERT)
    
    @allure.step("Get text of alert")
    def get_text_alert(self):
        return self.get_text_element(self.ALERT)