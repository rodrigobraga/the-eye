from rest_framework import mixins, status, viewsets
from rest_framework.permissions import AllowAny
from rest_framework.response import Response


class Healthcheck(viewsets.GenericViewSet):
    permission_classes = (AllowAny,)

    def retrieve(self, request, *args, **kwargs):
        return Response(status=status.HTTP_200_OK)
