from pages.base_page import BasePage
import time
import allure

class Search(BasePage):

    INPUT_SEARCH = ('xpath','//input[@name="search"]')   
    BUTTON_SEARCH = ('css selector','#search > button')
    PRODUCTS_SEARCH_RESULT = ('class name', 'col.mb-3')
    H1_TEXT = ('tag name','h1')

    ASSERT_SEARCH_TEXT_IN_SEARCHING_ITEMS = "Текст поиска отсутствует в найденных товарах"
    ASSERT_SEARCH_TEXT_NOT_IN_SEARCHING_ITEMS = "Текст поиска есть в найденных товарах"
    ASSERT_SEARCH_TEXT_IN_H1 = "Текст поиска есть в заголовке H1"
    ASSERT_SEARCH_TEXT_NOT_IN_H1 = "Текст поиска отсутствует в заголовке H1"

    @allure.step('Input text in search input')
    def enter_text_to_search_input(self, text):
        self.enter_text(self.INPUT_SEARCH, text)

    @allure.step("Click button search")
    def click_button_search(self):
        self.click_on_element(self.BUTTON_SEARCH)

    def search_result(self, text):
        result1 = self.get_text_elements(self.PRODUCTS_SEARCH_RESULT)
        result = [res.lower() for res in result1]
        for elem in result:
            if text in elem:
                pass
            return True
    
    @allure.step("Check name item in heading tag")
    def check_h1_page(self):
        return self.get_text_element(self.H1_TEXT)  