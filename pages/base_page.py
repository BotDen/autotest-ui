from abc import ABC
from urllib.parse import urljoin

import allure
from playwright.sync_api import Page, expect

from config import settings
from data.constants import TIMEOUT_MULTIPLIER


class BasePage(ABC):
    """Базовый класс для страниц"""

    TITLE = ""
    URL = "/"

    def __init__(self, page: Page):
        self.page = page
        self.title = self.page.get_by_role("heading", name=self.TITLE)

    @property
    def url(self) -> str:
        return urljoin(settings.http_client.client_url, self.URL)

    def open_url(self, timeout: int = 50000):
        """Открытие нужного адреса"""
        with allure.step("Переходим по URL"):
            self.page.goto(self.url, timeout=timeout)

    def wait_page_url(self, timeout: int = 30, endpoint: str = ""):
        expected_url = urljoin(self.url, endpoint)
        with allure.step(f"Ожидаем отображение страницы и проверяем ее url == {expected_url}"):
            self.page.wait_for_url(expected_url, timeout=timeout * TIMEOUT_MULTIPLIER)

    def check_open(self):
        """Проверка открытия страницы"""
        self.wait_page_url()

    def check_title(self):
        """Проверка заголовка страницы"""
        with allure.step(f"Проверяем заголовок страницы {self.TITLE}"):
            expect(self.title).to_have_text(self.TITLE)
