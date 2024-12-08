from _5_3_base_contact import BaseContact
from faker import Faker

class BusinessContact(BaseContact):
    def __init__(self):
        super().__init__()
        faker = Faker()
        self.company = faker.company()
        self.position = faker.job()

    def __str__(self):
        return f'{super().__str__()}|{self.company} - {self.position}'