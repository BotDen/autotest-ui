import allure
from playwright.sync_api import expect

from pages.base_page import BasePage


class MainPage(BasePage):
    """Главная страница"""

    TITLE = "Added!"
    CONTINUE_SHOPPING = "Continue Shopping"
    URL = ""

    def __init__(self, page):
        super().__init__(page)
        self.nav_bar = self.page.locator(".nav")
        self.login = self.page.get_by_role("link", name=" Signup / Login")
        self.cart = self.page.get_by_role("link", name="Cart")
        self._modal = self.page.locator("#cartModal")
        self.add_to_cart_btn = self.page.locator(".productinfo")

    def open_login_page(self):
        """Переход на страницу входа/регистрации аккаунта"""
        with allure.step("Переходим на страницу вход/регистрация аккаунта"):
            self.login.click()

    def open_cart_page(self):
        """Переходим на страницу корзины"""
        with allure.step("Переходим в корзину"):
            self.cart.click()

    def add_one_item_to_cart(self, item: str):
        """Добавление одного элемента в корзину"""
        log_text = ""
        with allure.step(f"Добавляем в корзину {item}"):
            self.add_to_cart_btn.locator(f"a[data-product-id='{item}']").first.click()

    def add_items_to_cart(self, items: list):
        """Добавление нескольких товаров в корзину"""

        with allure.step("Добавляем товары в корзину"):
            for product_id in items:
                add_to_cart_btn = self.page.query_selector(f"a[data-product-id='{product_id}']")

                if add_to_cart_btn:
                    add_to_cart_btn.click()

                    self._modal.wait_for(timeout=5000)
                    expect(self._modal.filter().locator(".modal-title")).to_have_text(self.TITLE)
                    self._modal.get_by_role("button", name=self.CONTINUE_SHOPPING).click()
