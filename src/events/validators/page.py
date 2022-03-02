from enum import Enum
import logging

from events.validators.base import Creator, Validator

logger = logging.getLogger(__name__)


class PageViewValidator(Validator):
    def validate(self, raw: dict) -> bool:
        host: str = raw.get("host", {})

        if host != "www.consumeraffairs.com":
            logger.error(
                "Invalid host",
                extra=dict(
                    category=self.category,
                    event_type=self.name,
                    host=host,
                ),
            )
            return False

        return True


class CTAValidator(Validator):
    def validate(self, raw: dict) -> bool:
        element: str = raw.get("element", "")

        elements = ["chat bubble", "buy button"]

        if element not in elements:
            logger.error(
                "Invalid element",
                extra=dict(
                    category=self.category,
                    event_type=self.name,
                    element=element,
                ),
            )
            return False

        return True


class PageViewValidatorCreator(Creator):
    def factory(self) -> Validator:
        return PageViewValidator(category="form interaction", name="submit")


class CTAValidatorCreator(Creator):
    def factory(self) -> Validator:
        return CTAValidator(category="form interaction", name="cta click")
