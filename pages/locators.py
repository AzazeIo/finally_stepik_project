from selenium.webdriver.common.by import By


class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    BASKET_BUTTON_SHOW = (By.CSS_SELECTOR, ".btn-group a")
    BASKET_FORM_SHOW = (By.CSS_SELECTOR, "#basket_formset")
    BASKET_MESSAGE_SHOW = (By.CSS_SELECTOR, "#content_inner")


class LoginPageLocators:
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")
    LOGIN_INPUT = (By.CSS_SELECTOR, "#id_registration-email")
    PASSWORD_INPUT_ONE = (By.CSS_SELECTOR, "#id_registration-password1")
    PASSWORD_INPUT_TWO = (By.CSS_SELECTOR, "#id_registration-password2")
    REGISTRATION_BUTTON = (By.CSS_SELECTOR, "#register_form .btn-primary")


class ProductPageLocators:
    BASKET_BUTTON = (By.CSS_SELECTOR, ".btn-add-to-basket")
    PRODUCT_NAME_IN_STORE = (By.CSS_SELECTOR, "#content_inner h1:first-child")
    PRODUCT_NAME_IN_BASKET = (By.CSS_SELECTOR, "#messages div.alertinner strong")
    PRODUCT_PRICE_IN_STORE = (By.CSS_SELECTOR, "#content_inner p.price_color")
    PRODUCT_PRICE_IN_BASKET = (By.CSS_SELECTOR, ".alert-info p:first-child strong")
    SUCSSESEFUL_MESSAGE = (By.CSS_SELECTOR, "#messages div:first-child")
