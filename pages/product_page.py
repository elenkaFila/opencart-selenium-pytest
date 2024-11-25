from pages.base_page import BasePage
import time
import allure

class ProductPage(BasePage):

    PAGE_URL = 'http://localhost/index.php?route=product/product&language=en-gb&product_id=31&path=33'
    #PAGE_URL = 'http://localhost/index.php?route=product/product&language=en-gb&product_id=30&path=33'
    BREADCRUMB_PRODUCT = ('css selector',".breadcrumb-item:last-child a")
    H1_PRODUCT = ('tag name',"h1")
    MAIN_PHOTO_PRODUCT = ('css selector',".image img.mb-3")
    BUTTON_ADD_TO_CART_PROD_PAGE = ('id', 'button-cart')
    BUTTON_ADD_TO_WISHLIST_PROD_PAGE = ('css selector','.btn-group button:first-child')
    BUTTON_ADD_TO_COMPARE_PROD_PAGE = ('css selector','.btn-group button:last-child')
    INPUT_QUANTITY = ('id','input-quantity')
    SELECT_COLOR = ('id',"input-option-226")
    ALERT = ('class name', "alert.alert-success.alert-dismissible")
    ALERT_ADD_TO_CART_TEXT = "to your shopping cart!"
    ALERT_ADD_TO_WISHLIST_TEXT = "You must login or create an account to save"
    ALERT_ADD_TO_COMPARE_TEXT =  "to your product comparison!"
    BUTTON_CART_HEADER = ('css selector','#header-cart button.dropdown-toggle')
    PRODUCTS_IN_CART_HEADER = ('css selector','td.text-start')

    TITLE_PAGE = 'Nikon D300'
    ASSERT_PROD_TITLE_PAGE =  f'Наименование страницы не {TITLE_PAGE}'
    ASSERT_WRONG_BREADCRUMBS = 'Неправильные breadcrumbs'
    ASSERT_NO_PHOTO = 'Отсутствует фото товара'
    ASSERT_PROD_ALERT_COMPARE_NOT_PRESENT = 'Отсутствует alert о добавлении товара к сравнению'
    ASSERT_PROD_ALERT_WISHLIST_NOT_PRESENT ='Отсутствует alert о добавлении товара в список желаний'
    ASSERT_PROD_ALERT_ADD_CART_NOT_PRESENT ='Отсутствует alert о добавлении товара в корзину'
    ASSERT_PROD_ALERT_DIFFERENT_TEXT = 'Текст алерта не соответствует ожидаемому'
    ASSERT_PRODUCT_NOT_IN_CART_HEADER = 'Товар отсутствует в корзине'

    @allure.step('Name item in breadcrumbs is present')
    def check_breadcrumb(self):
        if self.get_text_element(self.BREADCRUMB_PRODUCT) == self.get_text_element(self.H1_PRODUCT):
            return True
        
    def get_product_name(self):
        return self.get_text_element(self.H1_PRODUCT)

    @allure.step('Check item in cart header')
    def check_product_in_button_cart_header(self):
        self.wait_alert_invisible(self.ALERT)
        self.click_on_element(self.BUTTON_CART_HEADER)        
        products = self.get_text_elements(self.PRODUCTS_IN_CART_HEADER)
        for prod in products:
            if self.get_product_name() == prod:
                return True
        
    @allure.step('Check photo item is present')
    def present_photo_product(self):
        self.element_is_present(self.MAIN_PHOTO_PRODUCT)
        return True
    
    @allure.step("Click add to wishlist button item")
    def add_to_wishlist(self):
        self.click_on_element(self.BUTTON_ADD_TO_WISHLIST_PROD_PAGE)
    
    @allure.step("Click add to compare button item")
    def add_to_compare(self):
        self.click_on_element(self.BUTTON_ADD_TO_COMPARE_PROD_PAGE)

    @allure.step("Click add to cart button item")
    def add_to_cart(self):
        self.click_on_element(self.BUTTON_ADD_TO_CART_PROD_PAGE)

    @allure.step('Enter quantities of item')
    def enter_quantities(self, text):
        self.enter_text(self.INPUT_QUANTITY,text)