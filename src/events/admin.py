import json

from django.contrib import admin
from django.utils.safestring import mark_safe

from pygments import highlight
from pygments.formatters.html import HtmlFormatter
from pygments.lexers.data import JsonLexer

from events.models import Event


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    """Admin panel to navigate over events"""

    fields = (
        "application",
        "event_id",
        "session_id",
        "category",
        "name",
        "data_prettified",
        "timestamp",
        "is_valid",
        "created_at",
        "updated_at",
    )

    list_display = (
        "application",
        "event_id",
        "session_id",
        "category",
        "name",
        "timestamp",
        "is_valid",
    )

    list_filter = (
        "application__name",
        "category",
        "is_valid",
        "timestamp",
    )

    search_fields = (
        "event_id",
        "session_id",
        "category",
        "name",
        "application__name",
    )

    def get_readonly_fields(self, request, obj=None):
        return [field.name for field in self.model._meta.fields] + [
            "data_prettified"
        ]

    def has_add_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return False

    @admin.display(description="payload")
    def data_prettified(self, instance):
        """Function to display pretty version of data"""

        # Convert the data to sorted, indented JSON
        response = json.dumps(instance.data, sort_keys=True, indent=2)

        # Truncate the data.
        response = response[:10000]

        # Get the Pygments formatter
        formatter = HtmlFormatter(style="colorful")

        # Highlight the data
        response = highlight(response, JsonLexer(), formatter)

        # Get the stylesheet
        style = "<style>" + formatter.get_style_defs() + "</style><br />"

        # Safe the output
        return mark_safe(style + response)
