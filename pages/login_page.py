import allure

from pages.base_page import BasePage


class LoginPage(BasePage):
    """Страница входа/регистрации аккаунта"""

    URL = "login"

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

    def fill_form(self, email: str, name: str):
        """Заполняет поля 'Name' и 'Email' для регистрации аккаунта"""
        with allure.step(f"Заполняем поля 'Name' и 'Email' значениями '{name}' и '{email}'"):
            self.name.fill(name)
            self.signup_email.fill(email)

    def signup(self):
        """Нажимает кнопку 'Signup'"""
        with allure.step("Нажимаем на кнопку 'Signup'"):
            self.btn_signup.click()

    def login(self, email: str, password: str):
        """Вход в аккаунт"""
        with allure.step(f"Входим в аккаунт с email: {email} и password: {password}"):
            self.login_email.fill(email)
            self.login_password.fill(password)
            self.btn_login.click()
