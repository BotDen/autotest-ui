import allure
from playwright.sync_api import expect

from pages.base_page import BasePage


class DonePage(BasePage):
    """Страница подтверждения оформления заказа"""

    TITLE = "Order Placed!"
    TEXT = "Congratulations! Your order has been confirmed!"

    def __init__(self, page):
        super().__init__(page)
        self.title = self.page.get_by_role("heading", name=self.TITLE)
        self.text = self.page.locator(".col-sm-9 p")

    def check_text(self):
        """Проверяет текст на странице"""
        with allure.step(f"Проверяем, что текст '{self.TEXT}' отображается на странице"):
            expect(self.text).to_have_text(self.TEXT)
