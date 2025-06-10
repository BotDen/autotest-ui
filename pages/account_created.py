from playwright.sync_api import expect

from data.data import Url
from pages.base_page import BasePage


class AccountCreated(BasePage):

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

    def check_open(self):
        expect(self.page).to_have_url(Url.account_created_url)

    def check_title(self):
        expect(self.title).to_have_text(self.TITLE)

    def check_text(self):
        self.congratulations.is_visible()
        self.you_can.is_visible()

    def click_continue(self):
        self.btn_continue.click()
