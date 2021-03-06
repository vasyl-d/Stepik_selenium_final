from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):

    def is_product_page(self):
        self.should_be_add_to_basket()
        self.should_be_product_name()
        self.should_be_product_price()
        self.should_be_basket_button()
        self.add_to_basket()
        self.should_be_name_messages()
        self.should_be_name_correct()    
        self.should_be_price_messages()
        self.should_be_price_correct()


    def add_to_basket(self):
        ''' добавление товара в корзину. перед єтим запоминаем название и цену товара на его странице'''
        basket_butt = self.browser.find_element(*ProductPageLocators.PRODUCT_ADD_BASKET)
        self.product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text
        self.product_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text
        basket_butt.click()
        #для решения задач с капечей в алерте нужно раскомментить
        #self.solve_quiz_and_get_code()
        
    def should_be_add_to_basket(self):
        assert self.is_element_present(*ProductPageLocators.PRODUCT_ADD_BASKET), "Не нашли кнопку добавления в корзину " + self.error_msg

    def should_be_product_name(self):
        assert self.is_element_present(*ProductPageLocators.PRODUCT_NAME), "Не нашли название товара " + self.error_msg

    def should_be_product_price(self):
        assert self.is_element_present(*ProductPageLocators.PRODUCT_PRICE), "Не нашли цену товара " + self.error_msg

    def should_be_basket_button(self):
        assert self.is_element_present(*ProductPageLocators.BASKET_BUTTON), "Не нашли ссылку на карзину " + self.error_msg

    def should_be_name_messages(self):
        assert self.is_element_present(*ProductPageLocators.ALERT_PRODUCT_NAME), "Не нашли сообщение с названием " + self.error_msg

    def should_be_name_correct(self):
        product_name = self.browser.find_element(*ProductPageLocators.ALERT_PRODUCT_NAME).text
        assert (product_name == self.product_name), "Название не совападает " + product_name + "<>" + self.product_name 
    
    def should_be_price_messages(self):
        assert self.is_element_present(*ProductPageLocators.ALERT_PRODUCT_PRICE), "Не нашли сообщение с ценой " + self.error_msg

    def should_be_price_correct(self):
        product_price = self.browser.find_element(*ProductPageLocators.ALERT_PRODUCT_PRICE).text
        assert (product_price == self.product_price), "Цена не совпадает " + product_price + "<>" + self.product_price
    
    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), "Сообщение об успехе присутствует "

    def should_message_dissapeared(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), "Сообщение не исчезло после тайм-аута"