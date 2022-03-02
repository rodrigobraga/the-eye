from events.validators import get_validator
from events.validators.default import DefaultValidator, DefaultValidatorCreator
from events.validators.page import PageViewValidator


class TestGetValidator:
    def test_get_validator(self):
        validator = get_validator("page interaction", "pageview")

        assert isinstance(validator, PageViewValidator)

    def test_get_default_validator(self):
        validator = get_validator("unknown", "unknown")

        assert isinstance(validator, DefaultValidator)


class TestDefaultValidator:
    def test_validate(self):
        validator = DefaultValidatorCreator().factory()

        assert validator.validate({}) is True


class TestFormValidator:
    def test_validate(self):
        validator = get_validator("form interaction", "submit")

        assert validator.validate({"form": {"first_name": "John"}})
        assert not validator.validate({"form": {"first_name": "John" * 256}})


class TestPageViewValidator:
    def test_validate(self):
        validator = get_validator("page interaction", "pageview")

        assert validator.validate({"host": "www.consumeraffairs.com"})
        assert not validator.validate({"host": "www.test.com"})


class TestCTAValidator:
    def test_validate(self):
        validator = get_validator("page interaction", "cta click")

        assert validator.validate({"element": "chat bubble"})
        assert not validator.validate({"element": "foo bar"})
