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
    mr = "Mr."
    mrs = "Mrs."

class CheckBox(str, Enum):
    newsletter = "#newsletter"
    from_partners = "#optin"

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
    usa = "United State"
    india = "India"
    canada = "Canada"

class CanadaState(str, Enum):
    ontario = "Ontario"
    quebec = "Quebec"
    nova_scotia = "Nova Scotia"
    manitoba = "Manitoba"

class CanadaCity(str, Enum):
    brandon = "Brandon"
    gimli = "Gimli"

class Items(Enum):
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
