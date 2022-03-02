from functools import lru_cache

from events.validators.base import Validator
from events.validators.default import DefaultValidator
from events.validators.form import FormValidatorCreator
from events.validators.page import (
    CTAValidatorCreator,
    PageViewValidatorCreator,
)

MAPPER = {
    "page interaction": {
        "pageview": PageViewValidatorCreator,
        "cta click": CTAValidatorCreator,
    },
    "form interaction": {
        "submit": FormValidatorCreator,
    },
}


@lru_cache(maxsize=None)
def get_validator(category: str, name: str) -> Validator:
    """
    Get a validator for a given category and name.

    :param category: The category of the validator.
    :param name: The name of the validator.
    :return: The validator.
    """
    creator = MAPPER.get(category, {}).get(name, None)  # type: ignore

    if not creator:
        return DefaultValidator(category, name)

    return creator().factory()
