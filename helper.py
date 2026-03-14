from faker import Faker

faker = Faker()

def generate_registration_data():
    """Генерирует email, пароль и имя для регистрации."""
    name = faker.name()
    email = faker.email()
    password = faker.password()
    return name, email, password
