import logging

from drf_spectacular.types import OpenApiTypes
from drf_spectacular.utils import OpenApiExample, extend_schema
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from events.tasks import integrate

logger = logging.getLogger(__name__)


class EventView(APIView):
    @extend_schema(
        examples=[
            OpenApiExample(
                "sample",
                value={
                    "session_id": "e2085be5-9137-4e4e-80b5-f1ffddc25423",
                    "category": "page interaction",
                    "name": "pageview",
                    "data": {
                        "host": "www.consumeraffairs.com",
                        "path": "/",
                    },
                    "timestamp": "2021-01-01 09:15:27.243860",
                },
            )
        ],
        request=OpenApiTypes.JSON_PTR,
        responses={202: None},
    )
    def post(self, request, *args, **kwargs):
        user = request.user
        application = user.application
        payload = request.data

        integrate.delay(application.id, payload)

        logger.info(
            f"event received",
            extra=dict(application=application, payload=payload),
        )

        return Response(status=status.HTTP_202_ACCEPTED)
