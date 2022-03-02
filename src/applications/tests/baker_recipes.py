from faker import Faker
from model_bakery.recipe import Recipe, foreign_key

from applications.models import Application

fake = Faker()


application = Recipe(
    Application, name=fake.company(), user=foreign_key("users.tests.user")
)
