from playwright.sync_api import expect

from data.data import Url
from pages.base_page import BasePage


class SignupPage(BasePage):
    """Страница ввода данных аккаунта"""

    def __init__(self, page):
        super().__init__(page)
        self.gender = self.page.locator(".clearfix")
        self.password = self.page.get_by_label("password")
        self.day = self.page.locator("#days")
        self.month = self.page.locator("#months")
        self.year = self.page.locator("#years")
        self.check_box = self.page.get_by_role("checkbox")
        self.first_name = self.page.locator("#first_name")
        self.last_name = self.page.locator("#last_name")
        self.address1 = self.page.locator("#address1")
        self.country = self.page.get_by_label("country")
        self.state = self.page.locator("#state")
        self.city = self.page.locator("#city")
        self.zipcode = self.page.locator("#zipcode")
        self.mobile_number = self.page.locator("#mobile_number")
        self.btn_create = self.page.get_by_role("button", name="Create Account")

    def check_open(self):
        """Проверяем открытие страницы"""
        expect(self.page).to_have_url(Url.signup_url)

    def choose_gender(self, gender: str):
        """Выбираем пол"""
        self.gender.get_by_role("radio", name=gender).click()

    def fill_password(self, password: str):
        """Вводим пароль"""
        self.password.fill(password)

    def choose_date_of_birth(self, day: str, month: str, year: str):
        """Вводим дату рождения"""
        self.day.select_option(day)
        self.month.select_option(month)
        self.year.select_option(year)

    def choose_check_box(self, checkbox: str):
        """Выбираем дополнительные подписки"""
        self.page.query_selector(checkbox)

    def fill_name(self, first_name: str, last_name: str):
        """Вводим фамилию и имя"""
        self.first_name.fill(first_name)
        self.last_name.fill(last_name)

    def fill_address1(self, address: str):
        """Вводим адрес"""
        self.address1.fill(address)

    def choose_country(self, country: str):
        """Вводим страну"""
        self.country.select_option(country)

    def fill_state(self, state: str):
        """Вводим штат"""
        self.state.fill(state)

    def fill_city(self, city: str):
        """Вводим город"""
        self.city.fill(city)

    def fill_zipcode(self, zipcode: str):
        """Вводим почтовый индекс"""
        self.zipcode.fill(zipcode)

    def fill_mobile_number(self, number: str):
        """Вводим номер телефона"""
        self.mobile_number.fill(number)

    def click_btn_create_account(self):
        """Нажимаем кнопку 'Created account'"""
        self.btn_create.click()
