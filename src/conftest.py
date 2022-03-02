from model_bakery import baker
import pytest
from rest_framework.test import APIClient
from rest_framework_simplejwt.tokens import RefreshToken


@pytest.fixture
def user():
    application = baker.make_recipe("applications.tests.application")

    return application.user


@pytest.fixture
def access_token(user):
    refresh = RefreshToken.for_user(user)

    return {"refresh": str(refresh), "access": str(refresh.access_token)}


@pytest.fixture
def client(access_token):
    token = access_token.get("access")
    client = APIClient()
    client.credentials(HTTP_AUTHORIZATION=f"Bearer {token}")

    return client
