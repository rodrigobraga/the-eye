from model_bakery import baker
import pytest


@pytest.mark.django_db
class TestApplication:
    def test_str(self):
        application = baker.make_recipe(
            "applications.tests.application", name="Test Application"
        )

        assert str(application) == "Test Application"
