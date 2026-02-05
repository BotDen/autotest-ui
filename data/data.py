from dataclasses import dataclass


class Url:
    main_url = "https://automationexercise.com/"
    login_url = f"{main_url}login"
    signup_url = f"{main_url}signup"
    account_created_url = f"{main_url}account_created"
    cart_url = f"{main_url}view_cart"
    checkout_url = f"{main_url}checkout"
    payment_url = f"{main_url}payment"
    done_url = f"{main_url}payment_done/0"


class User:
    user_name = "Dim"
    user_email = "mail1234564@mail.ru"
    password = "123456"
    first_name = "Dima"
    last_name = "Sidorov"
    address1 = "street 43"
    zipcode = "ROC OCO"
    mobile_number = "+12505550199"

class Gender:
    mr = "Mr."
    mrs = "Mrs."

class CheckBox:
    newsletter = "#newsletter"
    from_partners = "#optin"

class Months:
    JANUARY = "January"
    FEBRUARY = "February"
    MARCH = "March"
    APRIL = "April"
    MAY = "May"
    JUNE = "June"
    JULY = "July"
    AUGUST = "August"
    SEPTEMBER = "September"
    OCTOBER = "October"
    NOVEMBER = "November"
    DECEMBER = "December"

class Country:
    usa = "United State"
    india = "India"
    canada = "Canada"

class CanadaState:
    ontario = "Ontario"
    quebec = "Quebec"
    nova_scotia = "Nova Scotia"
    manitoba = "Manitoba"

class CanadaCity:
    brandon = "Brandon"
    gimli = "Gimli"

class Items:
    blue_top = "1"
    men_tshirt = 2
    sleeveless_dress = 3
    stylish_dress = 4

@dataclass
class Card:
    number: str
    month: str
    year: str
    cvc: str
