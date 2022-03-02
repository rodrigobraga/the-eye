import json

from django.core.management.base import BaseCommand, CommandError

from rest_framework_simplejwt.tokens import RefreshToken

from users.models import User


class Command(BaseCommand):
    help = "Generate token for a user"

    def add_arguments(self, parser):
        parser.add_argument("email", type=str)

    def handle(self, *args, **options):
        email = options["email"]

        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            message = self.style.ERROR(f"User unknown: {email}")

            self.stderr.write(message)

            raise CommandError(message)
        else:
            refresh = RefreshToken.for_user(user)

            data = json.dumps(
                {
                    "refresh": str(refresh),
                    "access": str(refresh.access_token),
                }
            )

            message = self.style.SUCCESS(data)

            self.stdout.write(message)
