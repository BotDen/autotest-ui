from playwright.sync_api import expect

from data.data import Url
from pages.base_page import BasePage


class LoginPage(BasePage):

    def __init__(self, page):
        super().__init__(page)
        self._signup_form = self.page.locator(".signup-form")
        self.name = self._signup_form.get_by_placeholder("Name")
        self.signup_email = self._signup_form.get_by_placeholder("Email Address")
        self.btn_signup = self._signup_form.get_by_role("button", name="Signup")
        self._login_form = self.page.locator(".login-form")
        self.login_email = self._login_form.get_by_placeholder("Email Address")
        self.login_password = self._login_form.get_by_placeholder("Password")
        self.btn_login = self._login_form.get_by_role("button", name="Login")

    def check_open(self):
        expect(self.page).to_have_url(Url.login_url)

    def fill_form(self, name: str, email: str):
        self.name.fill(name)
        self.signup_email.fill(email)

    def signup(self):
        self.btn_signup.click()

    def login(self, email: str, password: str):
        self.login_email.fill(email)
        self.login_password.fill(password)
        self.btn_login.click()
