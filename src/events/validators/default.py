from events.validators.base import Creator, Validator


class DefaultValidator(Validator):
    """A dumb validator that always returns True"""

    def validate(self, data: dict) -> bool:
        return True


class DefaultValidatorCreator(Creator):
    def factory(self) -> Validator:
        return DefaultValidator(category="unknown", name="unknown")
