from dataclasses import dataclass
from enum import Enum


class User:
    user_name = "Dim"
    user_email = "mail1234564@mail.ru"
    password = "123456"
    first_name = "Dima"
    last_name = "Sidorov"
    address1 = "street 43"
    zipcode = "ROC OCO"
    mobile_number = "+12505550199"


class Gender(str, Enum):
    MR = "Mr."
    MRS = "Mrs."


class CheckBox(str, Enum):
    NEWS_LETTER = "#newsletter"
    FROM_PARTNERS = "#optin"


class Months(str, Enum):
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


class Country(str, Enum):
    USA = "United State"
    INDIA = "India"
    CANADA = "Canada"


class CanadaState(str, Enum):
    ONTARIO = "Ontario"
    QUEBEC = "Quebec"
    NOVA_SCOTIA = "Nova Scotia"
    MANITOBA = "Manitoba"


class CanadaCity(str, Enum):
    BRANDON = "Brandon"
    GIMLI = "Gimli"


class ItemsInt(int, Enum):
    BLUE_TOP = 1
    MEN_TSHIRT = 2
    SLEEVELESS_DRESS = 3
    STYLISH_DRESS = 4


class ItemsStr(str, Enum):
    BLUE_TOP = "Blue top"
    MEN_TSHIRT = "Men tshirt"
    SLEEVELESS_DRESS = "Sleeveless dress"
    STYLISH_DRESS = "Stylish dress"


@dataclass
class Card:
    number: str
    month: str
    year: str
    cvc: str
