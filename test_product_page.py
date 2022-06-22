from .pages.login_page import LoginPage
from .pages.product_page import ProductPage
from .pages.basket_page import BasketPage
import pytest
import time

class TestProductToBasket():

    # Для задания с прогоном акционных товаров с параметром, можно задаь урлы:
    # product_base_link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"
    # urls = [f"{product_base_link}?promo=offer{no}" if no != "???"
    #    else pytest.param("bugged_link", marks=pytest.mark.xfail) for no in range(10)]
    #@pytest.mark.parametrize('link', urls)

    @pytest.mark.need_review
    @pytest.mark.parametrize('link', ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"])
    def test_guest_can_add_product_to_basket(self, browser, link ):
        page = ProductPage(browser, link)
        page.open()
        page.is_product_page()

    @pytest.mark.xfail(reason="xfail пользователь должен видеть сообщение о добавлении товара")
    def test_guest_cant_see_success_message_after_adding_product_to_basket(self, browser):
        url = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
        page = ProductPage(browser, url, timeout=1)
        page.open()
        page.add_to_basket()
        page.should_not_be_success_message()

    def test_guest_cant_see_success_message(self, browser):
        url = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
        page = ProductPage(browser, url, timeout=1)
        page.open()
        page.should_not_be_success_message()

    @pytest.mark.xfail(reason="xfail сообщение и не должно исчезать")
    def test_message_disappeared_after_adding_product_to_basket(self, browser): 
        url = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
        page = ProductPage(browser, url, timeout=0)
        page.open()
        page.add_to_basket()
        page.should_message_dissapeared()

    def test_guest_should_see_login_link_on_product_page(self, browser):
        link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
        page = ProductPage(browser, link)
        page.open()
        page.should_be_login_link()

    @pytest.mark.need_review
    def test_guest_can_go_to_login_page_from_product_page(self, browser):
        link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
        page = ProductPage(browser, link)
        page.open() 
        page.go_to_login_page()

    @pytest.mark.need_review
    def test_guest_cant_see_product_in_basket_opened_from_product_page(self, browser):
        link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
        page = ProductPage(browser, link)
        page.open()
        page.should_be_basket_link()
        page.go_to_basket()
        b_page = BasketPage(browser, browser.current_url)
        b_page.should_be_basket_empty()
        b_page.should_empty_message_present()


@pytest.mark.login
class TestUserAddToBasketFromProductPage():
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        link = "http://selenium1py.pythonanywhere.com/accounts/login/"
        page = LoginPage(browser, link)
        page.open()
        password = str(time.time())
        login = password + "@wasa.org"
        page.register_new_user(login, password)
        page.should_be_authorized_user()

    @pytest.mark.need_review
    def test_user_can_add_product_to_basket(self, browser):
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
        page = ProductPage(browser, link)
        page.open()
        page.is_product_page()

    def test_user_cant_see_success_message(self, browser):
        url = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
        page = ProductPage(browser, url, timeout=0)
        page.open()
        page.should_not_be_success_message()
