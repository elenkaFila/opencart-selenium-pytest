from pages.main_page import MainPage
import pytest
import time
import allure

@allure.feature('Main page tests')
class TestMainPage:
    
    def setup_method(self):
        self.main_page = MainPage(self.driver)

    @allure.story('Common')
    @allure.title('Check title page')  
    def test_title(self):
        self.main_page.open()
        assert self.main_page.get_title_page() == self.main_page.TITLE_PAGE, self.main_page.ASSERT_MAIN_TITLE_PAGE

    

    @allure.story('Labels block')
    @allure.title('Check labels are present')  
    def test_label_list_exists(self):
        self.main_page.open()
        assert self.main_page.exist_label_list() == True, self.main_page.ASSERT_MAIN_LIST_LABELS

    @allure.story('Swiper block')
    @allure.title('Check picture changes click on bullets')
    def test_change_picture_by_swiper_bullet(self):
        self.main_page.open()
        prew_link = self.main_page.get_picture_src()
        self.main_page.click_swiper_bullet()
        actual_link = self.main_page.get_picture_src()
        assert actual_link != prew_link, self.main_page.ASSERT_MAIN_PICTURE_CHANGE

    @allure.story('Swiper block')
    @allure.title('Check picture changes click on arrow previous')
    def test_change_picture_by_swiper_arrow_prev(self):
        self.main_page.open()
        prew_link = self.main_page.get_picture_src()
        self.main_page.click_swiper_arrow_previous()
        actual_link = self.main_page.get_picture_src()
        assert actual_link != prew_link, self.main_page.ASSERT_MAIN_PICTURE_CHANGE

    @allure.story('Swiper block')
    @allure.title('Check picture changes click on arrow next')
    def test_click_by_swiper_arrow_next(self):
        self.main_page.open()
        prew_link = self.main_page.get_picture_src()
        self.main_page.click_swiper_arrow_next()
        actual_link = self.main_page.get_picture_src()
        assert actual_link != prew_link, self.main_page.ASSERT_MAIN_PICTURE_CHANGE
    
    @allure.story('Currency block')
    @allure.title('Check curency changes in items and menu')
    def test_change_currency(self):
        self.main_page.open()
        self.main_page.click_currency_menu()
        # список валют
        all_currencies_text = self.main_page.get_all_currencies()
        for currency in all_currencies_text:
            self.main_page.driver.find_element('xpath',f'//*[text()="{currency}"]').click()
            text = currency.split(" ", 1)[0] 
            assert text == self.main_page.get_current_currency(), 'Не получилось поменять валюту'
            # проверяем карточки товаров на наличие в них выбранной валюты
            for price_type in (self.main_page.PRODUCT_PRICE_CURRENCY,self.main_page.PRODUCT_PRICE_TAX_CURRENCY):
                for price_elem in self.main_page.driver.find_elements(*price_type):
                    assert text in price_elem.text, f"В цене {price_elem.text} отсутствует валюта {text}"
            self.main_page.click_currency_menu()

    @allure.story('Feature block')
    @allure.title('Count feature items')
    def test_featured_count(self):
        self.main_page.open()
        assert self.main_page.count_feature_elements() == 4, self.main_page.ASSERT_MAIN_COUNT_ITEMS

    @allure.story('Feature block')
    @allure.title('Add to compare item alert is present')
    def test_compare_button(self):
        self.main_page.open()
        self.main_page.add_to_compare()
        assert self.main_page.present_alert() == True, self.main_page.ASSERT_MAIN_ALERT_COMPARE_NOT_PRESENT
        assert self.main_page.ALERT_ADD_TO_COMPARE_TEXT in self.main_page.get_text_alert(), self.main_page.ASSERT_MAIN_ALERT_DIFFERENT_TEXT

    @allure.story('Feature block')
    @allure.title('Add to cart item alert is present')
    def test_add_to_cart_button(self):
        self.main_page.open()
        self.main_page.add_to_cart()
        assert self.main_page.present_alert() == True, self.main_page.ASSERT_MAIN_ALERT_ADD_CART_NOT_PRESENT
        assert self.main_page.ALERT_ADD_TO_CART_TEXT in self.main_page.get_text_alert(), self.main_page.ASSERT_MAIN_ALERT_DIFFERENT_TEXT
    
    @allure.story('Feature block')
    @allure.title('Add to wishlist item alert is present')
    def test_add_to_wishist(self):
        self.main_page.open()
        self.main_page.add_to_wishlist()
        assert self.main_page.present_alert() == True, self.main_page.ASSERT_MAIN_ALERT_WISHLIST_NOT_PRESENT
        assert self.main_page.ALERT_ADD_TO_WISHLIST_TEXT in self.main_page.get_text_alert(), self.main_page.ASSERT_MAIN_ALERT_DIFFERENT_TEXT