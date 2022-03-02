from celery import shared_task
from celery.utils.log import get_task_logger

from events.models import Event

logger = get_task_logger(__name__)


@shared_task
def integrate(application_id: int, payload: dict):

    Event.objects.create(application_id=application_id, **payload)

    logger.info(
        "event integrated",
        extra=dict(application_id=application_id, payload=payload),
    )

    return "event integrated"
