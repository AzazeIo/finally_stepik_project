from .base_page import BasePage
from .locators import MainPageLocators


class BasketPage(BasePage):
    def guest_go_to_basket_page(self):
        basket_button_show = self.browser.find_element(*MainPageLocators.BASKET_BUTTON_SHOW)
        basket_button_show.click()

    def guest_see_empty_basket_page(self):
        assert self.is_not_element_present(*MainPageLocators.BASKET_FORM_SHOW), "The basket is not empty"

    def guest_see_basket_empty_message(self):
        assert self.is_element_present(*MainPageLocators.BASKET_MESSAGE_SHOW), "The basket empty message is absent"