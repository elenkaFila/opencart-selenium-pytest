from pages.base_page import BasePage
import time
import allure

class UserLogin(BasePage):
    
    PAGE_URL = "http://localhost/index.php?route=account/login&language=en-gb"
    INPUT_EMAIL = ('id',"input-email")
    INPUT_PASSWORD = ('id',"input-password")
    BUTTON_CONTINUE = ('xpath','//*[text()="Continue"]')
    BUTTON_LOGIN = ('xpath','//button[text()="Login"]')
    ERROR_EMAIL = ('id',"error-email")
    ERROR_PASSWORD = ('id',"error-password")
    ALERT_ERRORS = ('class name', "alert.alert-danger.alert-dismissible")
    ALERT_ERRORS_TEXT = 'Warning: No match for E-Mail Address and/or Password.'
    URL_AFTER_LOGIN = "http://localhost/index.php?route=account/account&language=en-gb&customer_token="
    TITLE_PAGE = "Account Login"

    ASSERT_LOGIN_TITLE_PAGE = "Наименование страницы не 'Account Login'"
    ASSERT_LOGIN_NO_ALERT = 'Отсутствует алерт при пустом логине'
    ASSERT_LOGIN_ALERT_DIFFERENT_TEXT = 'Текст алерта не соответствует ожидаемому'
    ASSERT_LOGIN_FAIL = 'Пользователь не смог залогиниться'

    @allure.step('Enter email: [{text}]')
    def enter_email(self, text):
        self.enter_text(self.INPUT_EMAIL, text)
    
    @allure.step('Enter password: [{text}]')
    def enter_password(self, text):
        self.enter_text(self.INPUT_PASSWORD, text)
    
    @allure.step('Click button login')
    def click_button_login(self):
        self.click_on_element(self.BUTTON_LOGIN)

    @allure.step('Click button continue')
    def click_button_continue(self):
        self.click_on_element(self.BUTTON_CONTINUE)

    def get_url_after_login(self):
        return self.get_current_url(self.URL_AFTER_LOGIN)


    @allure.step("Alert is present")
    def present_alert(self):
        return self.element_is_present(self.ALERT_ERRORS)
    
    @allure.step("Get text of alert")
    def get_text_alert(self):
        return self.get_text_element(self.ALERT_ERRORS)
    
