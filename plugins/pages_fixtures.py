import allure
import pytest
from playwright.sync_api import Page

from pages.account_created import AccountCreated
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage
from pages.done_page import DonePage
from pages.login_page import LoginPage
from pages.main_page import MainPage
from pages.payment_page import PaymentPage
from pages.signup_page import SignupPage


@allure.title("Инициализация MainPage")
@pytest.fixture
def main_page(page: Page) -> "MainPage":
    return MainPage(page)


@allure.title("Инициализация LoginPage")
@pytest.fixture
def login_page(page: Page) -> "LoginPage":
    return LoginPage(page)


@allure.title("Инициализация CheckoutPage")
@pytest.fixture
def checkout_page(page: Page) -> "CheckoutPage":
    return CheckoutPage(page)


@allure.title("Инициализация CartPage")
@pytest.fixture
def cart_page(page: Page) -> "CartPage":
    return CartPage(page)


@allure.title("Инициализация PaymentPage")
@pytest.fixture
def payment_page(page: Page) -> "PaymentPage":
    return PaymentPage(page)


@allure.title("Инициализация DonePage")
@pytest.fixture
def done_page(page: Page) -> "DonePage":
    return DonePage(page)


@allure.title("Инициализация SingupPage")
@pytest.fixture
def signup_page(page: Page) -> "SignupPage":
    return SignupPage(page)


@allure.title("Инициализация AccountCreatedPage")
@pytest.fixture
def account_created_page(page: Page) -> "AccountCreated":
    return AccountCreated(page)
