from events.validators import get_validator
from events.validators.base import Validator


def validate_handler(sender, instance, created, **kwargs):
    """Validate payload from an event when is applicable"""
    if not created:
        return

    validator: Validator = get_validator(instance.category, instance.name)

    instance.is_valid = validator.validate(instance.data)
    instance.save(update_fields=["is_valid"])
