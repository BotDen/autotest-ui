import allure

from data.data import User, Items


@allure.link("Ссылка на тест кейс")
def test_add_item_to_cart(
    main_page,
    login_page,
    checkout_page,
):
    main_page.open_url()
    main_page.check_open()
    main_page.open_login_page()
    login_page.check_open()
    login_page.login(
        email=User.user_email,
        password=User.password,
    )
    main_page.add_items_to_cart([Items.blue_top, Items.stylish_dress])
    main_page.open_cart_page()
    checkout_page.check_items_in_cart(["Blue top", "Stylish dress"])
