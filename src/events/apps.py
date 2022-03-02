from django.apps import AppConfig
from django.db.models.signals import post_save


class EventsConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "events"

    def ready(self):
        from events.receivers import validate_handler

        post_save.connect(validate_handler, sender="events.Event")
