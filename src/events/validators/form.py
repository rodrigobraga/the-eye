import logging

from events.validators.base import Creator, Validator

logger = logging.getLogger(__name__)


class FormValidator(Validator):
    def validate(self, raw: dict) -> bool:
        form: dict = raw.get("form", {})
        first_name: str = form.get("first_name", "")

        if len(first_name) > 255:
            logger.error(
                "Invalid first name",
                extra=dict(
                    category=self.category,
                    event_type=self.name,
                    first_name=first_name,
                ),
            )
            return False

        return True


class FormValidatorCreator(Creator):
    def factory(self) -> Validator:
        return FormValidator(category="form interaction", name="submit")
