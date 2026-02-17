import allure
import pytest

from data.data import Gender, Months, CheckBox, Country, CanadaState, CanadaCity
from tools.allure.epic import AllureEpic
from tools.allure.features import AllureFeature
from tools.allure.stories import AllureStories
from tools.faker import fake


@allure.title("Successful registration new user")
@allure.epic(AllureEpic.REGISTRATION)
@allure.feature(AllureFeature.AUTHENTICATION)
@allure.story(AllureStories.REGISTRATION)
@pytest.mark.smok
@pytest.mark.regression
def test_success_registration_new_user(
    main_page,
    login_page,
    signup_page,
    account_created_page
):
    main_page.open_url()
    main_page.check_open()

    main_page.open_login_page()
    login_page.check_open()
    login_page.fill_form(
        email=fake.get_email(),
        name=fake.get_first_name(),
    )
    login_page.signup()
    signup_page.check_open()
    signup_page.choose_gender(Gender.MR)
    signup_page.fill_password(fake.get_password())
    signup_page.choose_date_of_birth(
        day="25",
        month=Months.APRIL,
        year="1988"
    )
    signup_page.choose_check_box(CheckBox.FROM_PARTNERS)
    signup_page.fill_name(
        first_name=fake.get_first_name(),
        last_name=fake.get_last_name(),
    )
    signup_page.fill_address1(fake.get_address())
    signup_page.choose_country(Country.CANADA)
    signup_page.fill_state(CanadaState.MANITOBA)
    signup_page.fill_city(CanadaCity.GIMLI)
    signup_page.fill_zipcode(fake.get_zip_code())
    signup_page.fill_mobile_number(fake.get_phone())
    signup_page.click_btn_create_account()
    account_created_page.check_open()
    account_created_page.check_title()
    account_created_page.check_text_congratulations()
    account_created_page.check_text_you_can()
    account_created_page.click_continue()
