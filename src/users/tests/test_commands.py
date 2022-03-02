from io import StringIO
from sys import stderr

from django.core.management import call_command
from django.core.management.base import CommandError

import pytest


@pytest.mark.django_db
class TestGetTokenForUser:
    def test_command_output(self, user):
        out = StringIO()

        call_command("get_tokens_for_user", user.email, stdout=out)

        result = out.getvalue()

        assert "refresh" in result
        assert "access" in result

    def test_command_output_fails_when_email_is_not_recognized(self):
        out = StringIO()

        with pytest.raises(CommandError):
            call_command("get_tokens_for_user", "foo@bar.io", stderr=out)

        result = out.getvalue()

        assert "User unknown: foo@bar.io" in result
