from faker import Faker

class BusinessCard:
    def __init__(self):
        faker = Faker()
        self.name = faker.name()
        self.last_name = faker.last_name()
        self.company = faker.company()
        self.position = faker.job()
        self.email = faker.email()

    def __str__(self):
        return f'{self.name} {self.last_name} | {self.company} - {self.position} | {self.email}'