import allure
import pytest

from data.data import Url, User, Items
from data.pay_cards import CARD_01


@pytest.mark.smoke
@allure.link("Ссылка на тест кейс")
def test_success_order_placement(
    main_page,
    login_page,
    cart_page,
    checkout_page,
    payment_page,
    done_page,
):
    main_page.go_to_url(timeout=50000)
    main_page.go_to_login()
    login_page.login(User.user_email, User.password)
    main_page.add_one_item_to_cart(Items.blue_top)
    main_page.go_to_cart()
    cart_page.check_open(Url.cart_url)
    cart_page.proceed_to_checkout()
    checkout_page.check_open(Url.checkout_url)
    checkout_page.check_items_in_cart(["Blue top"])
    checkout_page.place_order()
    payment_page.check_open(Url.payment_url)
    payment_page.fill_form_payment(
        first_name=User.first_name,
        last_name=User.last_name,
        card_number=CARD_01.number,
        month=CARD_01.month,
        year=CARD_01.year,
        cvc=CARD_01.cvc,
    )
    payment_page.pay_order()
    done_page.check_title()
    done_page.check_text()
