import allure
from playwright.sync_api import expect

from pages.base_page import BasePage


class PaymentPage(BasePage):
    """Страница оплаты заказа"""

    URL = "payment"
    ALERT_SUCCESS = "Your order has been placed successfully!"

    def __init__(self, page):
        super().__init__(page)
        self._payment_intput = self.page.locator(".payment-information")
        self.name = self._payment_intput.locator("[name='name_on_card']")
        self.card_number = self._payment_intput.locator("[name='card_number']")
        self.cvc = self._payment_intput.locator("[name='cvc']")
        self.expiration_month = self._payment_intput.locator("[name='expiry_month']")
        self.expiration_year = self._payment_intput.locator("[name='expiry_year']")
        self.btn_pay = self._payment_intput.get_by_role("button", name="Pay and Confirm Order")
        self.alert_success = self._payment_intput.locator(".alert-success")

    def fill_form_payment(self, first_name: str, last_name: str, card_number: str, cvc: str, month: str, year: str):
        """Заполнение полей для оплаты"""
        with allure.step("Заполняем поля для оплаты заказа"):
            with allure.step(f"Вводим имя first_name: {first_name} и last_name: {last_name}"):
                self.name.fill(f"{first_name} {last_name}")
            with allure.step(f"Вводим номер карты {card_number}"):
                self.card_number.fill(card_number)
            with allure.step(f"Вводим cvc карты {cvc}"):
                self.cvc.fill(cvc)
            with allure.step(f"Вводим месяц действия карты {month}"):
                self.expiration_month.fill(month)
            with allure.step(f"Вводим год действия карты {year}"):
                self.expiration_year.fill(year)

    def pay_order(self):
        """Оплата заказа"""
        with allure.step("Нажимаем на кнопку оплаты заказа"):
            self.btn_pay.click()
