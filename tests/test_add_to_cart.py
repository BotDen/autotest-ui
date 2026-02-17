import allure
import pytest

from data.data import ItemsStr, User, ItemsInt
from tools.allure.epic import AllureEpic
from tools.allure.features import AllureFeature
from tools.allure.stories import AllureStories


@allure.title("Successful addition of item to cart")
@allure.epic(AllureEpic.CLIENT)
@allure.feature(AllureFeature.USER)
@allure.story(AllureStories.ADD_ITEM)
@pytest.mark.regression
def test_success_add_item_to_cart(
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
    main_page.add_items_to_cart([ItemsInt.BLUE_TOP, ItemsInt.STYLISH_DRESS])
    main_page.open_cart_page()
    checkout_page.check_items_in_cart([ItemsStr.BLUE_TOP, ItemsStr.STYLISH_DRESS])
