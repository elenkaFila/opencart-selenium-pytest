from pages.registration_user_page import UserRegistration
from pages.main_page import MainPage
from selenium.webdriver.support import expected_conditions as EC
import pytest
import time
from faker import Faker
import csv
import allure

fake = Faker("ru_RU")

test_data = [(fake.first_name(),fake.last_name(), fake.email(), fake.password())
         ] 

@allure.feature('Registration user positive tests')
class TestsPositive:
    def setup_method(self):
        self.reg_user = UserRegistration(self.driver)
        self.main_page = MainPage(self.driver)

    @allure.story('Common functions')
    @allure.tag('positive')
    @allure.title('Check title page')   
    def test_title(self):
        self.reg_user.open()
        assert self.reg_user.get_title_page() == self.reg_user.TITLE_PAGE, self.reg_user.ASSERT_REG_TITLE_PAGE

    @allure.story('Common functions')
    @allure.tag('positive')
    @allure.title('Check click on logo go to main page')
    def test_click_logo_go_to_main_page(self):
        self.reg_user.open()
        self.reg_user.click_logo()
        assert self.reg_user.get_title_page() == self.main_page.TITLE_PAGE, self.main_page.ASSERT_MAIN_CLICK_ON_LOGO

    @allure.story('Register user')
    @allure.tag('positive')    
    @allure.title('Register new user [{fname}, {lname}]')
    @pytest.mark.parametrize('fname, lname, email, passw', test_data)
    def test_register_user_positive(self, fname, lname, email, passw):
        self.reg_user.open()
        self.reg_user.enter_first_name(fname)
        self.reg_user.enter_last_name(lname)
        self.reg_user.enter_email(email)
        self.reg_user.enter_password(passw)
        with open('./tests/test_data_user.csv', 'a', encoding='utf-8-sig', newline='') as file:
            writer = csv.writer(file,delimiter=";")
            writer.writerow([
            fname, lname, email, passw
            ])
        self.reg_user.scroll_to_button()        
        self.reg_user.click_subscribe()
        self.reg_user.click_agree()
        self.reg_user.click_button_continue()
        assert self.reg_user.URL_AFTER_REGISTRATION in self.reg_user.url_after_registration(), self.reg_user.ASSERT_REG_FAIL_REGISTRATION

@allure.feature('Registration user negative tests')    
class TestsNegative:
    def setup_method(self):
        self.reg_user = UserRegistration(self.driver)
        self.main_page = MainPage(self.driver)

    @allure.story('click button "continue"')        
    @allure.tag('negative')
    @allure.title('Click button "continue", wait alert policy')
    def test_register_user_with_empty_fields(self):
        self.reg_user.open()
        self.reg_user.scroll_to_button()
        self.reg_user.click_button_continue()
        assert self.reg_user.present_alert() == True, self.reg_user.ASSERT_REG_ALERT_PRIVACY_POLICY
        assert self.reg_user.get_text_alert() == self.reg_user.ALERT_POLICY_TEXT, self.reg_user.ASSERT_REG_ALERT_PRIVACY_POLICY_TEXT
        assert self.reg_user.present_all_errors() == True,  self.reg_user.ASSERT_REG_ALL_FIELDS_ERRORS

    @allure.story('click button and checkbox "subscribe"')        
    @allure.tag('negative')
    @allure.title('Click only button and checbox "subscribe", wait alert policy')
    def test_register_user_empty_fields_check_subscribe(self):
        self.reg_user.open()
        self.reg_user.scroll_to_button()        
        self.reg_user.click_subscribe()
        self.reg_user.click_button_continue()
        assert self.reg_user.present_alert() == True, self.reg_user.ASSERT_REG_ALERT_PRIVACY_POLICY
        assert self.reg_user.get_text_alert() == self.reg_user.ALERT_POLICY_TEXT, self.reg_user.ASSERT_REG_ALERT_PRIVACY_POLICY_TEXT
        assert self.reg_user.present_all_errors() == True,  self.reg_user.ASSERT_REG_ALL_FIELDS_ERRORS

    @allure.story('click button and checkboxes')
    @allure.tag('negative')
    @allure.title('Click button and all checboxes with empty fields')
    def test_register_user_empty_fields_check_subs_agree(self):
        self.reg_user.open()
        self.reg_user.scroll_to_button()
        self.reg_user.click_subscribe()
        self.reg_user.click_agree()
        self.reg_user.click_button_continue()
        assert self.reg_user.present_all_errors() == True, self.reg_user.ASSERT_REG_ALL_FIELDS_ERRORS
    
    @allure.story('correct first name input')
    @allure.tag('negative')
    @allure.title("Fill only first name input correct parametres: [{fname}]")
    @pytest.mark.parametrize('fname', [1, 'Коля', 'был обычный серый питерский', 'были обычные серые питерские'])
    def test_register_user_one_input_fname(self, fname):
        self.reg_user.open()
        self.reg_user.enter_first_name(fname)
        self.reg_user.scroll_to_button()
        self.reg_user.click_subscribe()
        self.reg_user.click_agree()
        self.reg_user.click_button_continue()
        assert self.reg_user.present_error_lname() and self.reg_user.present_error_email() and self.reg_user.present_error_password() == True, self.reg_user.ASSERT_REG_ALL_FIELDS_ERRORS

    @allure.story('incorrect first name input')
    @allure.tag('negative')
    @allure.title("Fill only first name input incorrect parametres: [{fname}]")
    @pytest.mark.parametrize('fname',['', ' ', 'очень длинный текст такого просто не бывает'])
    def test_register_user_one_input_fname_error(self, fname):
        self.reg_user.open()
        self.reg_user.enter_first_name(fname)
        self.reg_user.scroll_to_button()
        self.reg_user.click_subscribe()
        self.reg_user.click_agree()
        self.reg_user.click_button_continue()
        assert self.reg_user.present_all_errors() == True, self.reg_user.ASSERT_REG_ALL_FIELDS_ERRORS
    
    @allure.story('correct last name input')
    @allure.tag('negative')
    @allure.title("Fill only last name input correct parametres: [{lname}]")
    @pytest.mark.parametrize('lname', [1, 'Коля', 'был обычный серый питерский', 'были обычные серые питерские'])
    def test_register_user_one_input_lname(self, lname):
        self.reg_user.open()
        self.reg_user.enter_last_name(lname)
        self.reg_user.scroll_to_button()
        self.reg_user.click_subscribe()
        self.reg_user.click_agree()
        self.reg_user.click_button_continue()
        assert self.reg_user.present_error_fname() and self.reg_user.present_error_email() and self.reg_user.present_error_password() == True, self.reg_user.ASSERT_REG_ALL_FIELDS_ERRORS

    @allure.story('incorrect last name input')
    @allure.tag('negative')
    @allure.title("Fill only last name input correct parametres: [{lname}]")
    @pytest.mark.parametrize('lname',['', ' ', 'очень длинный текст такого просто не бывает'])
    def test_register_user_one_input_lname_error(self, lname):
        self.reg_user.open()
        self.reg_user.enter_last_name(lname)
        self.reg_user.scroll_to_button()
        self.reg_user.click_subscribe()
        self.reg_user.click_agree()
        self.reg_user.click_button_continue()
        assert self.reg_user.present_all_errors() == True, self.reg_user.ASSERT_REG_ALL_FIELDS_ERRORS

    @allure.story('correct email input')
    @allure.tag('negative')   
    @allure.title("Fill only email input correct parametr: [{email}]")
    @pytest.mark.parametrize('email', ['mail@mail.com'])
    def test_register_user_one_input_email(self, email):
        self.reg_user.open()
        self.reg_user.enter_email(email)
        self.reg_user.scroll_to_button()
        self.reg_user.click_subscribe()
        self.reg_user.click_agree()
        self.reg_user.click_button_continue()
        assert self.reg_user.present_error_fname() and self.reg_user.present_error_lname() and self.reg_user.present_error_password() == True, self.reg_user.ASSERT_REG_ALL_FIELDS_ERRORS

    @allure.story('incorrect email input')
    @allure.tag('negative')   
    @allure.title("Fill only email input incorrect parametres: [{email}], wait browser validation errors")
    @pytest.mark.parametrize('email', ['@mail', 's', 's@','Коля@mm.ru','okey@.dd'])
    def test_register_user_one_input_email_error_hint(self, email):
        self.reg_user.open()
        self.reg_user.enter_email(email)
        self.reg_user.scroll_to_button()
        self.reg_user.click_subscribe()
        self.reg_user.click_agree()
        self.reg_user.click_button_continue()
        assert self.reg_user.present_error_email_field_hint() is not None, self.reg_user.ASSERT_REG_EMAIL_FIELD_NO_ERROR_HINT

    @allure.story('incorrect email input') 
    @allure.tag('negative')       
    @allure.title("Fill only email input incorrect parametres:  [{email}], wait alert errors")
    @pytest.mark.parametrize('email',['',' ','oket@mail'])
    def test_register_user_one_input_email_error_hint_none(self, email):
        self.reg_user.open()
        self.reg_user.enter_email(email)
        self.reg_user.scroll_to_button()
        self.reg_user.click_subscribe()
        self.reg_user.click_agree()
        self.reg_user.click_button_continue()
        assert self.reg_user.unpresent_error_email_field_hint() == '', self.reg_user.ASSERT_REG_EMAIL_FIELD_ERROR_HINT
        assert self.reg_user.present_all_errors() == True, self.reg_user.ASSERT_REG_ALL_FIELDS_ERRORS
        
    
    