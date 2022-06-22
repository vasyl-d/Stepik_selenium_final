from .base_page import BasePage
from .locators import LoginPageLocators

class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        '''проверка на корректный url /login/''' 
        url = self.browser.current_url
        assert url.rfind("login") > 0, "Не корректный url"

    def should_be_login_form(self):
        ''' проверка, что есть форма логина '''
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Не нашли форму логиина: " + self.error_msg


    def should_be_register_form(self):
        ''' проверка, что есть форма регистрации на странице'''
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "Не нашли форму регистрации: " + self.error_msg

    def register_new_user(self, email, password):
        ''' регистрация нового пользователя на сайте'''
        is_reg = True
        try:
            e_email = self.browser.find_element(*LoginPageLocators.REGISTER_EMAIL)
            e_password1 = self.browser.find_element(*LoginPageLocators.REGISTER_PASS1)
            e_password2 = self.browser.find_element(*LoginPageLocators.REGISTER_PASS2)
            e_email.send_keys(email)
            e_password1.send_keys(password)
            e_password2.send_keys(password)
            self.browser.find_element(*LoginPageLocators.REGISTER_SUBMIT).click()
        except Exception as ex:
            self.error_msg = f"An exception of type {type(ex).__name__} случилось."
            is_reg = False
        assert is_reg, "Не удалось зарегать " + self.error_msg