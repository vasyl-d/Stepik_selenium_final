from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):

    def should_be_basket_empty(self):
        assert self.is_not_element_present(*BasketPageLocators.PRODUCT_IN_BASKET), 'Карзина не пуста'

    def should_empty_message_present(self):
        assert self.is_element_present(*BasketPageLocators.EMPTY_BASKET_MESSAGE), 'Нет сообщения что пусто'
