from selenium.webdriver.common.by import By
from .pages.product_page import ProductPage
import pytest

class TestProductToBasket():
    @pytest.mark.parametrize('link', ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
                                  pytest.param("bugged_link", marks=pytest.mark.xfail),
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"])

    # или если параметром можно задаь урлы:
    # product_base_link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"
    # urls = [f"{product_base_link}?promo=offer{no}" if no != "???"
    #    else pytest.param("bugged_link", marks=pytest.mark.xfail) for no in range(10)]
    # @pytest.mark.parametrize('link', urls)

    def test_guest_can_add_product_to_basket(self, browser, link ):
        #url = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
        #url = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
        page = ProductPage(browser, link)
        page.open()
        page.is_product_page()
