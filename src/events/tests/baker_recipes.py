from unicodedata import category

from django.utils import timezone

from faker import Faker
from model_bakery.recipe import Recipe, foreign_key

from events.models import Event

fake = Faker()


event = Recipe(
    Event,
    application=foreign_key("applications.tests.application"),
    event_id=fake.uuid4,
    session_id=fake.uuid4,
    category=fake.word,
    name=fake.word,
    data={
        "foo": fake.word(),
        "bar": fake.word(),
    },
    timestamp=timezone.localtime(),
)
