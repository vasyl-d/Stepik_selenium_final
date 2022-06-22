from .pages.main_page import MainPage 
from .pages.login_page import LoginPage
from .pages.basket_page import BasketPage 
import pytest

@pytest.mark.login
class TestMainPage1():

    def test_guest_should_see_login_link(self, browser):
        link = "http://selenium1py.pythonanywhere.com/"
        page = MainPage(browser, link)
        page.open()
        page.should_be_login_link()
        page.go_to_login_page()

    
    def test_guest_cant_see_product_in_basket_opened_from_main_page(self, browser):
        link = "http://selenium1py.pythonanywhere.com/"
        page = MainPage(browser, link)
        page.open()
        page.should_be_basket_link()
        page.go_to_basket()
        b_page = BasketPage(browser, browser.current_url)
        b_page.should_be_basket_empty()
        b_page.should_empty_message_present()


class TestLoginPage():

    def test_user_should_see_login_forms(self, browser):
        link = "http://selenium1py.pythonanywhere.com/accounts/login/"
        page = LoginPage(browser, link)
        page.open()
        page.should_be_login_url()
        page.should_be_login_form()
        page.should_be_register_form()