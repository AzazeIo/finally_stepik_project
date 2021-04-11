from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert "login" in self.browser.current_url, "login is absent in current url"

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not presented"

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "Register form is not presented"

    def register_new_user(self, email, password):
        login_input = self.browser.find_element(*LoginPageLocators.LOGIN_INPUT)
        login_input.send_keys(email)
        password_input_one = self.browser.find_element(*LoginPageLocators.PASSWORD_INPUT_ONE)
        password_input_one.send_keys(password)
        password_input_two = self.browser.find_element(*LoginPageLocators.PASSWORD_INPUT_TWO)
        password_input_two.send_keys(password)
        registration_button = self.browser.find_element(*LoginPageLocators.REGISTRATION_BUTTON)
        registration_button.click()
