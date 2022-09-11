from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from core.contrib.unique_none import get_unique_or_none


class Command(BaseCommand):
    help = "Create superuser for django."

    def add_q_admin(self, username, email, password):
        try:
            user = get_unique_or_none(User, username=username)

            if not user:
                user = User()
                user.email = email
            user.username = username
            user.is_superuser = True
            user.is_staff = True
            user.set_password(password)
            user.save()
        except User.DoesNotExist:
            pass

    def handle(self, *args, **options):
        self.add_q_admin('q-admin', 'q-admin@q-rest.hr', 'password')