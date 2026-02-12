import allure

from data.data import Url, User, Items


@allure.link("Ссылка на тест кейс")
def test_add_item_to_cart(
    main_page,
    login_page,
    checkout_page,
):
    main_page.go_to_url(timeout=50000)
    main_page.check_open(Url.main_url)
    main_page.go_to_login()
    login_page.check_open(Url.login_url)
    login_page.login(
        email=User.user_email,
        password=User.password,
    )
    main_page.add_items_to_cart([Items.blue_top, Items.stylish_dress])
    main_page.go_to_cart()
    checkout_page.check_items_in_cart(["Blue top", "Stylish dress"])
