from django.db import models
from django.utils import timezone


class TimeStampMixin(models.Model):
    """Tracking the time of changes in a instance"""

    created_at = models.DateTimeField("Created At", null=True, editable=False)
    updated_at = models.DateTimeField("Updated At", null=True, editable=False)

    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        now = timezone.localtime()

        if not self.created_at:
            self.created_at = now

        self.updated_at = now

        return super(TimeStampMixin, self).save(*args, **kwargs)
