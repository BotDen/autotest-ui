import allure

from pages.base_page import BasePage


class CartPage(BasePage):
    """Страница корзины с товаром"""

    def __init__(self, page):
        super().__init__(page)
        self.proceed_btn = self.page.get_by_text("Proceed To Checkout")

    def proceed_to_checkout(self):
        """Нажимает на кнпоку 'Proceed_to_checkout'"""
        with allure.step("Нажимаем на кнопку 'Proceed to checkout'"):
            self.proceed_btn.click()
