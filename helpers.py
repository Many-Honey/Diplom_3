from faker import Faker
faker = Faker('en_US')
class GenerateUserData:
    email = faker.email()
    name = faker.first_name()
    password = faker.password(10, special_chars=False, upper_case=False)

