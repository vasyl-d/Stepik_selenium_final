from selenium.webdriver.common.by import By
from .pages.main_page import MainPage 


class TestMainPage1():

#    def test_guest_can_go_to_login_page(self, browser):
#        link = "http://selenium1py.pythonanywhere.com/"
#        page = MainPage(browser, link)
#        page.open()                      # открываем страницу
#        page.go_to_login_page()          # выполняем метод страницы — переходим на страницу логина

    def test_guest_should_see_login_link(self, browser):
        link = "http://selenium1py.pythonanywhere.com/"
        page = MainPage(browser, link)
        page.open()
        page.should_be_login_link()
        print(page.error_msg)