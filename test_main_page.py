from selenium.webdriver.common.by import By
from .pages.main_page import MainPage 
from .pages.login_page import LoginPage 


class TestMainPage1():

#    def test_guest_can_go_to_login_page(self, browser):
#        link = "http://selenium1py.pythonanywhere.com/"
#        page = MainPage(browser, link)
#        page.open()                      # открываем страницу
#        page.go_to_login_page()          # выполняем метод страницы — переходим на страницу логина

    def test_guest_should_see_login_link(self, browser):
        #link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209?promo=midsummer"
        link = "http://selenium1py.pythonanywhere.com/"
        page = MainPage(browser, link)
        page.open()
        page.should_be_login_link()
        page.go_to_login_page()


class TestLoginPage():

    def test_user_should_see_login_forms(self, browser):
        page = LoginPage(browser, browser.current_url)
        page.should_be_login_url()
        page.should_be_login_form()
        page.should_be_register_form()