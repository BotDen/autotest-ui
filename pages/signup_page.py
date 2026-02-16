import allure

from pages.base_page import BasePage


class SignupPage(BasePage):
    """Страница ввода данных аккаунта"""

    URL = "signup"

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

    def choose_gender(self, gender: str):
        """Выбор пола"""
        with allure.step(f"Выбираем пол '{gender}'"):
            self.gender.get_by_role("radio", name=gender).click()

    def fill_password(self, password: str):
        """Ввод пароля"""
        with allure.step(f"Вводим пароль '{password}'"):
            self.password.fill(password)

    def choose_date_of_birth(self, day: str, month: str, year: str):
        """Ввод даты рождения"""
        with allure.step(f"Вводим дату рождения '{day, month, year}'"):
            self.day.select_option(day)
            self.month.select_option(month)
            self.year.select_option(year)

    def choose_check_box(self, checkbox: str):
        """Выбор дополнительной подписки"""
        with allure.step(f"Выбираем дополнительную подписку '{checkbox}'"):
            self.page.query_selector(checkbox)

    def fill_name(self, first_name: str, last_name: str):
        """Ввод фамилии и имени"""
        with allure.step(f"Вводим фамилию и имя '{last_name, first_name}'"):
            self.first_name.fill(first_name)
            self.last_name.fill(last_name)

    def fill_address1(self, address: str):
        """Ввод адреса"""
        with allure.step(f"Вводим адрес '{address}'"):
            self.address1.fill(address)

    def choose_country(self, country: str):
        """Ввод страны"""
        with allure.step(f"Вводим страну '{country}'"):
            self.country.select_option(country)

    def fill_state(self, state: str):
        """Ввод штата"""
        with allure.step(f"Вводим штат '{state}'"):
            self.state.fill(state)

    def fill_city(self, city: str):
        """Ввод города"""
        with allure.step(f"Вводим город '{city}'"):
            self.city.fill(city)

    def fill_zipcode(self, zipcode: str):
        """Ввод почтового индекса"""
        with allure.step(f"Вводим почтовый индекс '{zipcode}'"):
            self.zipcode.fill(zipcode)

    def fill_mobile_number(self, number: str):
        """Ввод номера телефона"""
        with allure.step(f"Вводим номер телефона '{number}'"):
            self.mobile_number.fill(number)

    def click_btn_create_account(self):
        """Нажимает кнопку 'Created account'"""
        with allure.step(f"Нажимаем на кнопку 'Created account'"):
            self.btn_create.click()
