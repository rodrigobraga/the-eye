from faker import Faker
from model_bakery.recipe import Recipe

from users.models import User

fake = Faker()


user = Recipe(User, email=fake.email())
