from pages.login_user_page import UserLogin
from pages.main_page import MainPage
import csv
import allure

@allure.feature('Login user')
class TestLoginUserPage:
  
    def setup_method(self):
        self.login_user = UserLogin(self.driver)
        self.main_page = MainPage(self.driver)
        
    @allure.story('Common')
    @allure.title('Check title page')
    def test_title(self):
        self.login_user.open()
        assert self.login_user.get_title_page() == self.login_user.TITLE_PAGE, self.login_user.ASSERT_LOGIN_TITLE_PAGE
    

    @allure.story('Common')
    @allure.title('Click on logo - go to main page')
    def test_click_logo_go_to_main_page(self):
        self.login_user.open()
        self.login_user.click_logo()
        assert self.login_user.get_title_page() == self.main_page.TITLE_PAGE, self.main_page.ASSERT_MAIN_CLICK_ON_LOGO
    

    @allure.story('Login user negative tests')
    @allure.title('User authorizathion with empty fields error alert is present')
    def test_login_user_empty_fields(self):
        self.login_user.open()
        self.login_user.click_button_login()
        assert self.login_user.present_alert() == True, self.login_user.ASSERT_LOGIN_NO_ALERT
        assert self.login_user.get_text_alert() == self.login_user.ALERT_ERRORS_TEXT, self.login_user.ASSERT_LOGIN_ALERT_DIFFERENT_TEXT
    
    @allure.story('Login user positive tests')
    @allure.title('User authorizathion')
    def test_login_user_positive(self):
        self.login_user.open()
        test_data=[]
        with open('./tests/test_data_user.csv','r',encoding='utf-8') as td:
            reader = csv.reader(td, delimiter=';')
            for row in reader:
                test_data.append(row)
            email = test_data[-2][2]
            passw = test_data[-2][3]
            self.login_user.enter_email(email)
            self.login_user.enter_password(passw)
            self.login_user.click_button_login()
            assert self.login_user.URL_AFTER_LOGIN in self.login_user.get_url_after_login(), self.login_user.ASSERT_LOGIN_FAIL
    
        
    