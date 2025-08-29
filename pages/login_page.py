import random
import string

import allure

from pages.base_page import BasePage


class LoginPage(BasePage):
    """Страница входа/регистрации аккаунта"""

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

    def generate_random_email(self, length=8):
        """Генерация случайного email"""
        characters = string.ascii_lowercase + string.digits
        random_username = ''.join(random.choice(characters) for _ in range(length))
        email = f"{random_username}@mail.ru"
        return email

    def fill_form(self, name: str):
        """Заполняет поля 'Name' и 'Email' для регистрации аккаунта"""
        email = self.generate_random_email()
        with allure.step(f"Заполняем поля 'Name' и 'Email' значениями '{name}' и '{email}'"):
            self.name.fill(name)
            self.signup_email.fill(email)

    def signup(self):
        """Нажимает кнопку 'Signup'"""
        with allure.step("Нажимаем на кнопку 'Signup'"):
            self.btn_signup.click()

    def login(self, email: str, password: str):
        """Вход в аккаунт"""
        with allure.step("Входим в аккаунт"):
            self.login_email.fill(email)
            self.login_password.fill(password)
            self.btn_login.click()
