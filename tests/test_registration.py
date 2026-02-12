import allure

from data.data import Url, User, Gender, Months, CheckBox, Country, CanadaState, CanadaCity


@allure.link("Ссылка на тест кейс")
def test_success_registration(
    main_page,
    login_page,
    signup_page,
    account_created_page
):
    main_page.go_to_url(timeout=50000)
    main_page.check_open(Url.main_url)
    main_page.go_to_login()
    login_page.check_open(Url.login_url)
    login_page.fill_form(name=User.user_name)
    login_page.signup()
    signup_page.check_open(Url.signup_url)
    signup_page.choose_gender(Gender.mr)
    signup_page.fill_password(User.password)
    signup_page.choose_date_of_birth(
        day="25",
        month=Months.APRIL,
        year="1988"
    )
    signup_page.choose_check_box(CheckBox.from_partners)
    signup_page.fill_name(
        first_name=User.first_name,
        last_name=User.last_name,
    )
    signup_page.fill_address1(User.address1)
    signup_page.choose_country(Country.canada)
    signup_page.fill_state(CanadaState.manitoba)
    signup_page.fill_city(CanadaCity.gimli)
    signup_page.fill_zipcode(User.zipcode)
    signup_page.fill_mobile_number(User.mobile_number)
    signup_page.click_btn_create_account()
    account_created_page.check_open(Url.account_created_url)
    account_created_page.check_title()
    account_created_page.check_text_congratulations()
    account_created_page.check_text_you_can()
    account_created_page.click_continue()
