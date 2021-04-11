from .pages.login_page import LoginPage
from .pages.product_page import ProductPage
from .pages.basket_page import BasketPage
import pytest
import time


class TestProductPage:
    def test_guest_cant_see_success_message(self, browser):
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
        page = ProductPage(browser, link)
        page.open()
        page.should_not_be_success_message()

    @pytest.mark.parametrize("promo_offer",
                             ["?promo=offer0",
                              "?promo=offer1",
                              "?promo=offer2",
                              "?promo=offer3",
                              "?promo=offer4",
                              "?promo=offer5",
                              "?promo=offer6",
                              pytest.param("?promo=offer7",
                                           marks=pytest.mark.xfail(reason="fixing this bug right now")),
                              "?promo=offer8",
                              "?promo=offer9"])
    @pytest.mark.need_review
    def test_guest_can_add_product_to_basket(self, browser, promo_offer):
        link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/{promo_offer}"
        page = ProductPage(browser, link)
        page.open()
        page.should_be_add_product_at_the_basket()
        page.solve_quiz_and_get_code()
        page.should_be_product_name_is_correct()
        time.sleep(2)
        page.should_be_product_price_is_correct()

    @pytest.mark.xfail(reason="Success message is present after adding product to basket")
    def test_guest_cant_see_success_message_after_adding_product_to_basket(self, browser):
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
        page = ProductPage(browser, link)
        page.open()
        page.should_be_add_product_at_the_basket()
        page.should_not_be_success_message()

    @pytest.mark.xfail(reason="Success message is not disappeared")
    def test_message_disappeared_after_adding_product_to_basket(self, browser):
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
        page = ProductPage(browser, link)
        page.open()
        page.should_be_add_product_at_the_basket()
        page.should_dissapear_of_success_message()

    def test_guest_should_see_login_link_on_product_page(self, browser):
        link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
        page = ProductPage(browser, link)
        page.open()
        page.should_be_login_link()

    @pytest.mark.need_review
    @pytest.mark.new
    def test_guest_can_go_to_login_page_from_product_page(self, browser):
        link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
        page = LoginPage(browser, link)
        page.open()
        page.go_to_login_page()
        page.should_be_login_page()

    @pytest.mark.need_review
    def test_guest_cant_see_product_in_basket_opened_from_product_page(self, browser):
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
        page = BasketPage(browser, link)
        page.open()
        page.guest_go_to_basket_page()
        page.guest_see_empty_basket_page()
        page.guest_see_basket_empty_message()


class TestUserAddToBasketFromProductPage:
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        link = "http://selenium1py.pythonanywhere.com/en-gb/accounts/login/"
        email = str(time.time()) + "@fakemail.org"
        password = str(time.time())
        self.page = LoginPage(browser, link)
        self.page.open()
        self.page.register_new_user(email, password)
        self.page.should_be_authorized_user()

    def test_user_cant_see_success_message(self, browser):
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
        page = ProductPage(browser, link)
        page.open()
        page.should_not_be_success_message()

    @pytest.mark.need_review
    def test_user_can_add_product_to_basket(self, browser):
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
        page = ProductPage(browser, link)
        page.open()
        page.should_be_add_product_at_the_basket()
        page.should_be_product_name_is_correct()
        time.sleep(2)
        page.should_be_product_price_is_correct()