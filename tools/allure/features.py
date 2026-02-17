from enum import Enum


class AllureFeature(str, Enum):
    USER = "user"
    AUTHENTICATION = "authentication"
    PAYMENT = "payment"
