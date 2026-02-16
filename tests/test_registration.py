import allure

from data.data import Gender, Months, CheckBox, Country, CanadaState, CanadaCity
from tools.faker import fake


@allure.link("Ссылка на тест кейс")
def test_success_registration(
    main_page,
    login_page,
    signup_page,
    account_created_page
):
    main_page.open_url()
    main_page.check_open()
    print(fake.get_random_birthday())
    main_page.open_login_page()
    login_page.check_open()
    login_page.fill_form(
        email=fake.get_email(),
        name=fake.get_first_name(),
    )
    login_page.signup()
    signup_page.check_open()
    signup_page.choose_gender(Gender.mr)
    signup_page.fill_password(fake.get_password())
    signup_page.choose_date_of_birth(
        day="25",
        month=Months.APRIL,
        year="1988"
    )
    signup_page.choose_check_box(CheckBox.from_partners)
    signup_page.fill_name(
        first_name=fake.get_first_name(),
        last_name=fake.get_last_name(),
    )
    signup_page.fill_address1(fake.get_address())
    signup_page.choose_country(Country.canada)
    signup_page.fill_state(CanadaState.manitoba)
    signup_page.fill_city(CanadaCity.gimli)
    signup_page.fill_zipcode(fake.get_zip_code())
    signup_page.fill_mobile_number(fake.get_phone())
    signup_page.click_btn_create_account()
    account_created_page.check_open()
    account_created_page.check_title()
    account_created_page.check_text_congratulations()
    account_created_page.check_text_you_can()
    account_created_page.click_continue()
