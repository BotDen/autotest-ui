import allure
from playwright.sync_api import expect

from pages.base_page import BasePage


class AccountCreated(BasePage):
    """Страница подтверждения оформления аккаунта"""

    TITLE = "Account Created!"
    CONGRATULATIONS = "Congratulations! Your new account has been successfully created!"
    YOU_CAN = """You can now take advantage of member privileges to 
    enhance your online shopping experience with us."""

    def __init__(self, page):
        super().__init__(page)
        self._container_success = self.page.locator(".row")
        self.title = self._container_success.locator(".title")
        self.congratulations = self._container_success.filter(has_text=self.CONGRATULATIONS)
        self.you_can = self._container_success.filter(has_text=self.YOU_CAN)
        self.btn_continue = self._container_success.locator(".btn-primary")

    def check_text_congratulations(self):
        """Проверка текста на странице"""
        with allure.step("Проверяем 'congratulations' текст на странице"):
            self.congratulations.is_visible()

    def check_text_you_can(self):
        """Проверка текста на странице"""
        with allure.step("Проверяем 'you_can' текст на странице"):
            self.you_can.is_visible()

    def click_continue(self):
        """Нажатие кнопки 'Continue'"""
        with allure.step("Нажимаем на кнопку 'Continue'"):
            self.btn_continue.click()
