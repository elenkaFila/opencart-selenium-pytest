from pages.base_page import BasePage
from selenium.webdriver.support import expected_conditions as EC
import time
import allure

class UserRegistration(BasePage):
    
    PAGE_URL = "http://localhost/index.php?route=account/register&language=en-gb"
    INPUT_FIRST_NAME = ('id',"input-firstname")
    INPUT_LAST_NAME = ('id',"input-lastname")
    INPUT_EMAIL = ('id',"input-email")
    INPUT_PASSWORD = ('id',"input-password")
    CHECKBOX_SUBSCRIBE = ('id',"input-newsletter")
    CHECKBOX_AGREE = ('xpath',"//*[@name='agree']")
    BUTTON_CONTINUE = ('xpath','//*[text()="Continue"]')
    ERROR_FNAME = ('id',"error-firstname")
    ERROR_LNAME = ('id',"error-lastname")
    ERROR_EMAIL = ('id',"error-email")
    ERROR_PASSWORD = ('id',"error-password")
    ALERT_POLICY = ('class name', "alert.alert-danger.alert-dismissible")
    ALERT_POLICY_TEXT = "Warning: You must agree to the Privacy Policy!"
    TITLE_PAGE = "Register Account"
    H1_AFTER_REGISTRATION = ('tag name','h1')
    H1_TEXT_AFTER_REGISTRATION = 'Your Account Has Been Created!'
    URL_AFTER_REGISTRATION = "http://localhost/index.php?route=account/success&language=en-gb&customer_token"

    ASSERT_REG_TITLE_PAGE = f'Наименование страницы не {TITLE_PAGE}'
    ASSERT_REG_ALERT_PRIVACY_POLICY = 'Отсутвует алерт о "privacy policy"'
    ASSERT_REG_ALERT_PRIVACY_POLICY_TEXT = f'Текст алерта о "privacy policy" не соответствует ожидаемому {ALERT_POLICY_TEXT}'
    ASSERT_REG_ALL_FIELDS_ERRORS = 'Отсутствуют ошибки валидации по пустым полям ввода'
    ASSERT_REG_EMAIL_FIELD_NO_ERROR_HINT = 'Отсутствует подсказка о неправильном заполнении поля email'
    ASSERT_REG_EMAIL_FIELD_ERROR_HINT = 'Присутствует подсказка о неправильном заполнении поля email'
    ASSERT_REG_FAIL_REGISTRATION = 'Регистрация пользователя не прошла'


    @allure.step("Enter first name: [{text}]")
    def enter_first_name(self,text):
        self.enter_text(self.INPUT_FIRST_NAME, text)
    
    @allure.step("Enter last name: [{text}]")
    def enter_last_name(self, text):
        self.enter_text(self.INPUT_LAST_NAME, text)

    @allure.step("Enter email: [{text}]")
    def enter_email(self, text):
        self.enter_text(self.INPUT_EMAIL, text)

    @allure.step("Enter password: [{text}]")
    def enter_password(self, text):
        self.enter_text(self.INPUT_PASSWORD, text)

    @allure.step("Click checkbox subscribe")
    def click_subscribe(self):
        self.click_on_element(self.CHECKBOX_SUBSCRIBE)

    @allure.step("Click checkbox agree policy")
    def click_agree(self):
        self.click_on_element(self.CHECKBOX_AGREE)
    
    @allure.step("Click button continue")
    def click_button_continue(self):
        self.click_on_element(self.BUTTON_CONTINUE)

    @allure.step("All errors of field are present")
    def present_all_errors(self):
        self.element_is_visible(self.ERROR_FNAME)
        self.element_is_visible(self.ERROR_LNAME)
        self.element_is_visible(self.ERROR_EMAIL)
        self.element_is_visible(self.ERROR_PASSWORD)
        return True

    @allure.step("Error field first name is present")
    def present_error_fname(self):
        self.element_is_visible(self.ERROR_FNAME)
        return True

    @allure.step("Error field last name is present")
    def present_error_lname(self):
        self.element_is_visible(self.ERROR_LNAME)
        return True
    
    @allure.step("Error field email is present")
    def present_error_email(self):
        self.element_is_visible(self.ERROR_EMAIL)
        return True

    @allure.step("Error field password is present")
    def present_error_password(self):
        self.element_is_visible(self.ERROR_PASSWORD)
        return True
          
    @allure.step("Check url after registration changed")
    def url_after_registration(self):
        return self.get_current_url(self.URL_AFTER_REGISTRATION)
        
    def scroll_to_button(self):
        self.scroll_to_element(self.BUTTON_CONTINUE)
    
    @allure.step("Error hint field email is present")
    def present_error_email_field_hint(self):
        self.wait.until(EC.text_to_be_present_in_element_attribute(self.INPUT_EMAIL,"validationMessage",' '))
        return self.element_get_attribute(self.INPUT_EMAIL,"validationMessage")
    
    @allure.step("Error hint field email is not present")
    def unpresent_error_email_field_hint(self):
        return self.element_get_attribute(self.INPUT_EMAIL,"validationMessage")
    
    @allure.step("Alert is present")
    def present_alert(self):
        return self.element_is_present(self.ALERT_POLICY)
    
    @allure.step("Get text of alert")
    def get_text_alert(self):
        return self.get_text_element(self.ALERT_POLICY)