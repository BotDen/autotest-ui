from playwright.sync_api import expect

from data.data import Url
from pages.base_page import BasePage


class CartPage(BasePage):
    """Страница корзины с товаром"""

    def __init__(self, page):
        super().__init__(page)
        self.proceed_btn = self.page.get_by_text("Proceed To Checkout")


    def check_open(self):
        expect(self.page).to_have_url(Url.cart_url)

    def proceed_to_checkout(self):
        self.proceed_btn.click()
