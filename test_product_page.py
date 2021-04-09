from .pages.product_page import ProductPage
import pytest


class TestProductPage():
    @pytest.mark.parametrize("promo_offer",
                             ["?promo=offer0",
                              "?promo=offer1",
                              "?promo=offer2",
                              "?promo=offer3",
                              "?promo=offer4",
                              "?promo=offer5",
                              "?promo=offer6",
                              pytest.param("?promo=offer7", marks=pytest.mark.xfail(reason="fixing this bug right now")),
                              "?promo=offer8",
                              "?promo=offer9"])
    def test_should_be_add_product_at_the_basket(self, browser, promo_offer):
        link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/{promo_offer}"
        page = ProductPage(browser, link)
        page.open()
        page.should_be_add_product_at_the_basket()
        page.solve_quiz_and_get_code()
        page.should_be_product_name_is_correct()
        page.should_be_product_price_is_correct()

    def test_guest_cant_see_success_message_after_adding_product_to_basket(self, browser):
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
        page = ProductPage(browser, link)
        page.open()
        page.should_be_add_product_at_the_basket()
        page.should_not_be_success_message()

    def test_guest_cant_see_success_message(self, browser):
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
        page = ProductPage(browser, link)
        page.open()
        page.should_not_be_success_message()

    def test_message_disappeared_after_adding_product_to_basket(self, browser):
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
        page = ProductPage(browser, link)
        page.open()
        page.should_be_add_product_at_the_basket()
        page.should_dissapear_of_success_message()
