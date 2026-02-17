from enum import Enum


class AllureStories(str, Enum):
    REGISTRATION = "Registration"
    LOGIN = "login"
    ADD_ITEM = "add item"
    PAY = "pay"
