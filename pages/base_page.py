from selenium.common.exceptions import NoAlertPresentException
import math
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC 
from selenium.common.exceptions import TimeoutException
from .locators import BasePageLocators

class BasePage():
    def __init__(self, browser, url, timeout=10):
        self.browser = browser
        self.url = url
        self.error_msg = ''
        self.browser.implicitly_wait(timeout)

    def open(self): 
        self.browser.get(self.url)

    def go_to_login_page(self):
        link = self.browser.find_element(*BasePageLocators.LOGIN_LINK)
        link.click()

    def should_be_login_link(self):
        assert self.is_element_present(*BasePageLocators.LOGIN_LINK), "Login link is not presented"

    def should_be_basket_link(self):
        assert self.is_element_present(*BasePageLocators.BASKET_VIEW), "Basket link is not presented"

    def go_to_basket(self):
        link = self.browser.find_element(*BasePageLocators.BASKET_VIEW)
        link.click()

    def is_element_present(self, how, what):
        #проверка присутствия єлемента на странице
        try:
            self.browser.find_element(how, what)
        except Exception as ex:
            self.error_msg = f"An exception of type {type(ex).__name__} случилось."
            return False
        return True

    def is_not_element_present(self, how, what, timeout=4):
        '''проверка что єлемента на странице нет
           (how, what) - это кортеж из locators
        '''
        try:
            WebDriverWait(self.browser, timeout).until(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return True

        return False

    def is_disappeared(self, how, what, timeout=4):
        ''' проверка, что єлемент исчезает со траницы
            (how, what) - это кортеж из locators
        '''
        try:
            WebDriverWait(self.browser, timeout, 1, TimeoutException).\
                until_not(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return False

        return True

    def solve_quiz_and_get_code(self):
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        try:
            alert = self.browser.switch_to.alert
            alert_text = alert.text
            print(f"Your code: {alert_text}")
            alert.accept()
        except NoAlertPresentException:
            print("No second alert presented")