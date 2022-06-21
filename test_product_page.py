from selenium.webdriver.common.by import By
from .pages.product_page import ProductPage
import pytest

class TestProductToBasket():
    #@pytest.mark.parametrize('link', ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
    #                              "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
    #                              "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
    #                              "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
    #                              "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
    #                              "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
    #                              "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
    #                              pytest.param("bugged_link", marks=pytest.mark.xfail),
    #                              "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8",
    #                              "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"])

    # или если параметром можно задаь урлы:
    # product_base_link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"
    # urls = [f"{product_base_link}?promo=offer{no}" if no != "???"
    #    else pytest.param("bugged_link", marks=pytest.mark.xfail) for no in range(10)]
    # @pytest.mark.parametrize('link', urls)

    @pytest.mark.skip(reason="на єтом шаге был пока не нужен")
    def test_guest_can_add_product_to_basket(self, browser, link ):
        #url = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
        #url = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
        page = ProductPage(browser, link)
        page.open()
        page.is_product_page()

    @pytest.mark.skip(reason="был xfail и должен падать")
    def test_guest_cant_see_success_message_after_adding_product_to_basket(self, browser):
        url = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
        page = ProductPage(browser, url, timeout=0)
        page.open()
        page.add_to_basket()
        page.should_not_be_success_message()

    @pytest.mark.skip(reason="на єтом шаге пропускаем")
    def test_guest_cant_see_success_message(self, browser):
        url = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
        page = ProductPage(browser, url, timeout=0)
        page.open()
        page.should_not_be_success_message()

    @pytest.mark.skip(reason="xfail сообщение и не должно исчезать")
    def test_message_disappeared_after_adding_product_to_basket(self, browser): 
        url = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
        page = ProductPage(browser, url, timeout=0)
        page.open()
        page.add_to_basket()
        page.should_message_dissapeared()

    def test_guest_should_see_login_link_on_product_page(self, browser):
        link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
        page = ProductPage(browser, link)
        page.open()
        page.should_be_login_link()

    def test_guest_can_go_to_login_page_from_product_page(self, browser):
        link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
        page = ProductPage(browser, link)
        page.open() 
        page.go_to_login_page()   
