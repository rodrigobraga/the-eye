import datetime
import uuid

from django.db import models
from django.forms import ValidationError
from django.utils import timezone

from core.models import TimeStampMixin


class Event(TimeStampMixin):
    """An event collected by The Eye"""

    application = models.ForeignKey(
        "applications.Application", on_delete=models.CASCADE
    )
    event_id = models.UUIDField(default=uuid.uuid4, editable=False)
    session_id = models.UUIDField(default=uuid.uuid4, editable=False)
    category = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    data = models.JSONField(default=dict)
    timestamp = models.DateTimeField()
    is_valid = models.BooleanField(default=True)

    class Meta:
        ordering = ("-timestamp",)

    def __str__(self):
        return f"{self.event_id}"

    def save(self, *args, **kwargs):
        if self.timestamp > timezone.localtime():
            raise ValidationError("Timestamp cannot be in the future")

        super(Event, self).save(*args, **kwargs)
