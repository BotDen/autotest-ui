from abc import ABC
from urllib.parse import urljoin

import allure
from playwright.sync_api import Page, expect

from config import settings


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

    def go_to_url(self, timeout: int | None = None):
        """Открытие нужного адреса"""
        with allure.step("Переходим по URL"):
            self.page.goto(self.url, timeout=timeout)

    def check_open(self, url):
        """Проверка открытия страницы"""
        with allure.step("Проверяем открытие страницы"):
            expect(self.page).to_have_url(url)

    def check_title(self):
        """Проверка заголовка страницы"""
        with allure.step(f"Проверяем заголовок страницы {self.TITLE}"):
            expect(self.title).to_have_text(self.TITLE)
