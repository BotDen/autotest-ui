from faker import Faker


class Fake:
    """Class for generating test data"""
    def __init__(self, faker: Faker):
        self.faker = faker

    def get_first_name(self) -> str:
        """Method for get first name"""
        return self.faker.first_name()

    def get_last_name(self) -> str:
        """Method for get last name"""
        return self.faker.last_name()

    def get_password(self) -> str:
        """Method for get password"""
        return self.faker.password()

    def get_email(self, domain: str | None = None) -> str:
        """Method for get email"""
        return self.faker.email(domain=domain)

    def get_phone(self) -> str:
        """Method for get a phone number"""
        return self.faker.phone_number()

    def get_zip_code(self) -> str:
        """Method for get a zip cose"""
        return self.faker.zipcode()

    def get_address(self) -> str:
        """Method for get address"""
        return self.faker.address()

    def get_random_birthday(self):
        """Method for get random birthday"""
        return self.faker.date_of_birth(minimum_age=18, maximum_age=59)

fake = Fake(faker=Faker())
