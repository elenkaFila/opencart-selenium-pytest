from pages.main_page import MainPage
from pages.search import Search
import pytest
import allure




class TestSearchFunction:
    
    def setup_method(self):
        self.main_page = MainPage(self.driver)
        self.search = Search(self.driver)

    @allure.feature('Search items negative tests')        
    @allure.tag('negative')
    @allure.title('Search items with parametres: [{text}]') 
    @pytest.mark.parametrize('text', [' ','','nothing'])
    def test_search_negative(self, text):
        self.main_page.open()
        self.search.enter_text_to_search_input(text)
        self.search.click_button_search()
        assert self.search.search_result(text) == None, self.search.ASSERT_SEARCH_TEXT_IN_SEARCHING_ITEMS
       
    @allure.feature('Search items positive tests')
    @allure.tag('positive')
    @allure.title('Search items with parametres: [{text}]') 
    @pytest.mark.parametrize('text', ['mac', '10.1', 'IPOD'])
    def test_search_positive(self, text):
        lower_text = text.lower()
        self.main_page.open()
        self.search.enter_text_to_search_input(text)
        self.search.click_button_search()
        assert self.search.search_result(lower_text) == True, self.search.ASSERT_SEARCH_TEXT_NOT_IN_SEARCHING_ITEMS
        assert self.search.check_h1_page() == f'Search - {text}', self.search.ASSERT_SEARCH_TEXT_NOT_IN_H1
