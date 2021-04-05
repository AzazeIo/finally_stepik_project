from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def should_be_add_product_at_the_basket(self):
        basket_button = self.browser.find_element(*ProductPageLocators.BASKET_BUTTON)
        basket_button.click()

    def should_be_product_name_is_correct(self):
        product_name_in_store = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME_IN_STORE)
        product_name_in_basket = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME_IN_BASKET)
        assert product_name_in_store.text == product_name_in_basket.text, "Product name is not correct"

    def should_be_product_price_is_correct(self):
        product_price_in_store = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE_IN_STORE)
        product_price_in_basket = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE_IN_BASKET)
        assert product_price_in_store.text == product_price_in_basket.text, "Product price is not correct"