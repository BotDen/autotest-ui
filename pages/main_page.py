from playwright.sync_api import expect

from data.data import Url
from pages.base_page import BasePage


class MainPage(BasePage):

    def __init__(self, page):
        super().__init__(page)
        self.nav_bar = self.page.locator(".nav")
        self.login = self.page.get_by_role("link", name=" Signup / Login")
        self._items = self.page.locator(".features_items")

    def check_open(self):
        expect(self.page).to_have_url(Url.main_url)

    def go_to_login(self):
        self.login.click()

    def add_item_to_cart(self, *args, **kwargs):
        