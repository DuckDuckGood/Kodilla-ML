from pydoc import classname

from faker import Faker

class BaseContact:
    def __init__(self):
        self.faker = Faker()
        self.first_name = self.faker.first_name()
        self.last_name = self.faker.last_name()
        self.phone_number = self.faker.phone_number()
        self.email = self.faker.email()

    def __str__(self):
        return f'{self.first_name} {self.last_name}|{self.phone_number}|{self.email}'

    def contact(self, other):
        print(f"I'll contact with {other}")

    @property
    def interview(self):
        return f'{type(self).__name__:<16}-> {self.__str__()}'

    @property
    def label_length(self):
        return len(f'{self.first_name} {self.last_name}')

    @property
    def _faker(self):
        return self.__faker

    @_faker.setter
    def _faker(self, f):
        self.__faker = f