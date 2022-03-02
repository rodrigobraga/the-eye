from unittest import mock

import pytest

from events.tasks import integrate


@pytest.mark.django_db
class TestIntegrate:
    @mock.patch("events.tasks.Event.objects.create")
    def test_integrate(self, mocker, user):
        application_id = user.application.id
        payload = {
            "session_id": "e2085be5-9137-4e4e-80b5-f1ffddc25423",
            "category": "page interaction",
            "name": "cta click",
            "data": {
                "host": "www.consumeraffairs.com",
                "path": "/",
                "element": "chat bubble",
            },
            "timestamp": "2021-01-01 09:15:27.243860Z",
        }

        integrate(application_id=application_id, payload=payload)

        mocker.assert_called_once_with(
            application_id=application_id, **payload
        )
