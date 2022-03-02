from django.conf import settings
from django.urls import reverse

import pytest
from rest_framework import status


@pytest.mark.django_db
class TestEventViewSet:
    @pytest.fixture(autouse=True)
    def set_up(self):
        settings.CELERY_TASK_ALWAYS_EAGER = True

    def test_post(self, client):
        url = reverse("event:events")

        data = {
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

        response = client.post(url, data, format="json")

        assert response.status_code == status.HTTP_202_ACCEPTED
