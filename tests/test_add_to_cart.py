from playwright.sync_api import Page

from data.data import Url, User, Items
from pages.checkout_page import CheckoutPage
from pages.login_page import LoginPage
from pages.main_page import MainPage


def test_add_item_to_cart(page: Page):
    main_page = MainPage(page)
    main_page.go_to_url(Url.main_url, timeout=50000)
    main_page.check_open()
    main_page.go_to_login()
    login_page = LoginPage(page)
    login_page.check_open()
    login_page.login(
        email=User.user_email,
        password=User.password,
    )
    main_page.add_items_to_cart([Items.blue_top, Items.stylish_dress])
    main_page.go_to_cart()
    checkout_page = CheckoutPage(page)
    checkout_page.check_items_in_cart(["Blue top", "Stylish dress"])
