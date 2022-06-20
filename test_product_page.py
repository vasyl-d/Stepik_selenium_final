from selenium.webdriver.common.by import By
from .pages.product_page import ProductPage

class TestProductToBasket():

    def test_guest_can_add_product_to_basket(self, browser):
        #url = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
        url = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
        page = ProductPage(browser, url)
        page.open()
        page.is_product_page()
