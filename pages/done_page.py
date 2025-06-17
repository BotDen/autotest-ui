from playwright.sync_api import expect

from data.data import Url
from pages.base_page import BasePage


class DonePage(BasePage):
    """Страница подтверждения оформления заказа"""

    TITLE = "Order Placed!"
    TEXT = "Congratulations! Your order has been confirmed!"

    def __init__(self, page):
        super().__init__(page)
        self.title = self.page.get_by_role("heading", name=self.TITLE)
        self.text = self.page.locator(".col-sm-9 p")

    def check_open(self):
        expect(self.page).to_have_url(Url.done_url)

    def check_title(self):
        expect(self.title).to_have_text(self.TITLE)

    def check_text(self):
        expect(self.text).to_have_text(self.TEXT)
