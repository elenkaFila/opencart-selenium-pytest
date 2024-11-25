from pages.base_page import BasePage
import time
import allure

class MainPage(BasePage):
    """Класс Главной страницы"""
    PAGE_URL = "http://localhost/"
    # активная картинка в слайдере
    PRODUCT_IMG = ('css selector', "#carousel-banner-0 .carousel-item.active img")
    
    # меню валюты
    #CURRENCY_MENU = ('xpath',"//div[@class='dropdown'][1]")
    # кружки для переключения в слайдере
    PRODUCT_SWIPER_BULLET = ("xpath", '(//button[@data-bs-target="#carousel-banner-0"])[2]')
    # стрелки для переключения в слайдере
    PRODUCT_SWIPER_ARROWS_PREVIOUS = ("css selector", "#carousel-banner-0 .carousel-control-prev")
    PRODUCT_SWIPER_ARROWS_NEXT = ("css selector", "#carousel-banner-0 .carousel-control-next")
    # предлагаемые товары и их цены
    FEATURED = ("css selector", ".col.mb-3")
    PRICE_NEW = ('class', "price-new")
    PRICE_TAX = ('class', "price-tax")
    # нижний слайдер с лейблами
    LABELS_CAROUSELE = ('id', "carousel-banner-0")
    ALERT = ('class name', "alert.alert-success.alert-dismissible")
    ALERT_ADD_TO_CART_TEXT = "to your shopping cart!"
    ALERT_ADD_TO_WISHLIST_TEXT = "You must login or create an account to save"
    ALERT_ADD_TO_COMPARE_TEXT =  "to your product comparison!"
    TITLE_PAGE = "Your Store"

    ASSERT_MAIN_TITLE_PAGE = f'Наименование страницы не {TITLE_PAGE}'
    ASSERT_MAIN_CLICK_ON_LOGO = 'Переход на главную страницу по клику на логотип не сработал'
    ASSERT_MAIN_COUNT_ITEMS = 'Некорректное количество предлагаемых товаров'
    ASSERT_MAIN_LIST_LABELS = "Отсутствует карусель с лейблами производителей на главной странице"
    ASSERT_MAIN_PICTURE_CHANGE = "Картинка отсутствует или не изменилась после свайпа"
    ASSERT_MAIN_ALERT_COMPARE_NOT_PRESENT = 'Отсутствует alert о добавлении товара к сравнению'
    ASSERT_MAIN_ALERT_WISHLIST_NOT_PRESENT ='Отсутствует alert о добавлении товара в список желаний'
    ASSERT_MAIN_ALERT_ADD_CART_NOT_PRESENT ='Отсутствует alert о добавлении товара в корзину'
    ASSERT_MAIN_ALERT_DIFFERENT_TEXT = 'Текст алерта не соответствует ожидаемому'

    
    
    def count_feature_elements(self):
        return self.count_elements(self.FEATURED)

    def exist_label_list(self):
        return self.element_is_present(self.LABELS_CAROUSELE)

    @allure.step('Click on right bullet')
    def click_swiper_bullet(self):
        self.click_on_element(self.PRODUCT_SWIPER_BULLET)

    @allure.step('Click on previous arrow')
    def click_swiper_arrow_previous(self):
        self.click_on_invisible_element(self.PRODUCT_SWIPER_ARROWS_PREVIOUS)

    @allure.step('Click on next arrow')
    def click_swiper_arrow_next(self):
        self.click_on_invisible_element(self.PRODUCT_SWIPER_ARROWS_NEXT)

    def get_picture_src(self):
        time.sleep(1)
        return self.element_get_attribute(locator=self.PRODUCT_IMG, attribute='src')

    @allure.step('Click on currency menu')
    def click_currency_menu(self):
        self.click_on_element(self.CURRENCY_MENU)

    def get_all_currencies(self):
        return self.get_text_elements(self.CURRENCIES)
        
    @allure.step('Get current currency')
    def get_current_currency(self):
        return self.get_text_element(self.CURENT_CURRENCY)

    @allure.step("Click add to wishlist button item")
    def add_to_wishlist(self):
        self.scroll_to_bottom_page(self.BUTTON_ADD_TO_WISHLIST_PRODUCT)
        self.click_on_element(self.BUTTON_ADD_TO_WISHLIST_PRODUCT)
    
    @allure.step("Click add to compare button item")
    def add_to_compare(self):
        self.scroll_to_bottom_page(self.BUTTON_ADD_TO_COMPARE_PRODUCT)
        self.click_on_element(self.BUTTON_ADD_TO_COMPARE_PRODUCT)

    @allure.step("Click add to cart button item")
    def add_to_cart(self):
        self.scroll_to_bottom_page(self.BUTTON_ADD_TO_CART_PRODUCT)
        self.click_on_element(self.BUTTON_ADD_TO_CART_PRODUCT)


    
    
        