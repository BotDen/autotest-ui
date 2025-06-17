from playwright.sync_api import Page

from data.data import Url, User, Items
from data.pay_cards import CARD_01
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage
from pages.done_page import DonePage
from pages.login_page import LoginPage
from pages.main_page import MainPage
from pages.payment_page import PaymentPage


def test_success_order_placement(page: Page):
    main_page = MainPage(page)
    main_page.go_to_url(Url.main_url, timeout=50000)
    main_page.go_to_login()
    login_page = LoginPage(page)
    login_page.login(User.user_email, User.password)
    main_page.add_one_item_to_cart(Items.blue_top)
    main_page.go_to_cart()
    cart_page = CartPage(page)
    cart_page.check_open()
    cart_page.proceed_to_checkout()
    checkout_page = CheckoutPage(page)
    checkout_page.check_open()
    checkout_page.check_items_in_cart(["Blue top"])
    checkout_page.place_order()
    payment_page = PaymentPage(page)
    payment_page.check_open()
    payment_page.fill_form_payment(
        first_name=User.first_name,
        last_name=User.last_name,
        card_number=CARD_01.number,
        month=CARD_01.month,
        year=CARD_01.year,
        cvc=CARD_01.cvc,
    )
    payment_page.pay_and_confirm_order()
    done_page = DonePage(page)
    done_page.check_title()
    done_page.check_text()
