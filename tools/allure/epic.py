from enum import Enum


class AllureEpic(str, Enum):
    CLIENT = "Client service"
    REGISTRATION = "Registration service"
    ORDER = "Order service"
