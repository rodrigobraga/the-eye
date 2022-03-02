from datetime import timedelta

from django.forms import ValidationError
from django.utils import timezone

from model_bakery import baker
import pytest


@pytest.mark.django_db
class TestEventModel:
    @pytest.fixture
    def application(self):
        return baker.make_recipe(
            "applications.tests.application", name="Test Application"
        )

    def test_str(self, application):
        event = baker.make_recipe(
            "events.tests.event",
            application=application,
            event_id="1eed6f44-cc1d-4d2d-814e-48b4f5cc91be",
        )

        assert str(event) == "1eed6f44-cc1d-4d2d-814e-48b4f5cc91be"

    def test_timestamp_validator(self, application):
        reference = timezone.localtime() + timedelta(days=1)

        with pytest.raises(ValidationError):
            baker.make_recipe(
                "events.tests.event",
                application=application,
                timestamp=reference,
            )
