from pages.product_page import ProductPage
import pytest
import time
import allure


class TestProductPage:
    
    def setup_method(self):
        self.product_page = ProductPage(self.driver)

    @allure.feature('Product page tests')
    @allure.story('Common')
    def test_elements_page(self):
        self.product_page.open()
        assert self.product_page.get_title_page() == self.product_page.TITLE_PAGE, self.product_page.ASSERT_PROD_TITLE_PAGE
        assert self.product_page.check_breadcrumb() == True, self.product_page.ASSERT_WRONG_BREADCRUMBS
        assert self.product_page.present_photo_product() == True, self.product_page.ASSERT_NO_PHOTO

    @allure.story('Buttons')
    @allure.title('Add to compare item alert is present')
    def test_compare_button(self):
        self.product_page.open()
        self.product_page.add_to_compare()
        assert self.product_page.present_alert() == True, self.product_page.ASSERT_PROD_ALERT_COMPARE_NOT_PRESENT
        assert self.product_page.ALERT_ADD_TO_COMPARE_TEXT in self.product_page.get_text_alert(), self.product_page.ASSERT_PROD_ALERT_DIFFERENT_TEXT

    @allure.story('Buttons')
    @allure.title('Add to cart item alert is present')
    def test_add_to_cart_button(self):
        self.product_page.open()
        self.product_page.add_to_cart()
        assert self.product_page.present_alert() == True, self.product_page.ASSERT_PROD_ALERT_ADD_CART_NOT_PRESENT
        assert self.product_page.ALERT_ADD_TO_CART_TEXT in self.product_page.get_text_alert(), self.product_page.ASSERT_PROD_ALERT_DIFFERENT_TEXT

    @allure.story('Buttons')
    @allure.title('Add to cart 3 items alert is present, items in cart are present')
    def test_add_to_cart_button_3_quantities(self):
        self.product_page.open()
        self.product_page.enter_quantities(5)
        self.product_page.add_to_cart()
        assert self.product_page.present_alert() == True, self.product_page.ASSERT_PROD_ALERT_ADD_CART_NOT_PRESENT
        assert self.product_page.ALERT_ADD_TO_CART_TEXT in self.product_page.get_text_alert(), self.product_page.ASSERT_PROD_ALERT_DIFFERENT_TEXT
        assert self.product_page.check_product_in_button_cart_header() == True, self.product_page.ASSERT_PRODUCT_NOT_IN_CART_HEADER

    @allure.story('Buttons')
    @allure.title('Add to wishlist item alert is present')
    def test_add_to_wishlist(self):
        self.product_page.open()
        self.product_page.add_to_wishlist()
        assert self.product_page.present_alert() == True, self.product_page.ASSERT_PROD_ALERT_WISHLIST_NOT_PRESENT 
        assert self.product_page.ALERT_ADD_TO_WISHLIST_TEXT in self.product_page.get_text_alert(), self.product_page.ASSERT_PROD_ALERT_DIFFERENT_TEXT