from playwright.sync_api import expect

from data.data import Url
from pages.base_page import BasePage


class MainPage(BasePage):
    """Главная страница"""

    MODAL_TITLE = "Added!"
    CONTINUE_SHOPPING = "Continue Shopping"

    def __init__(self, page):
        super().__init__(page)
        self.nav_bar = self.page.locator(".nav")
        self.login = self.page.get_by_role("link", name=" Signup / Login")
        self._modal = self.page.locator("#cartModal")

    def check_open(self):
        """Проверяем открытие страницы"""
        expect(self.page).to_have_url(Url.main_url)

    def go_to_login(self):
        """Переходим на страницу входа/регистрации аккаунта"""
        self.login.click()

    def add_item_to_cart(self, items: list):
        """Добавляем товар в корзину"""

        for product_id in items:
            add_to_cart_btn = self.page.query_selector(f"a[data-product-id='{product_id}']")

            if add_to_cart_btn:
                add_to_cart_btn.click()

                self._modal.wait_for(timeout=5000)
                expect(self._modal.filter().locator(".modal-title")).to_have_text(self.MODAL_TITLE)
                self._modal.get_by_role("button", name=self.CONTINUE_SHOPPING).click()
