from django.core.management.base import BaseCommand
from django.core.management import call_command
from django.db import transaction


class Command(BaseCommand):
    help = 'Loads all fixtures'

    @transaction.atomic
    def handle(self, *args, **options):
        call_command(
            'loaddata',
            'groups.yaml',
            'users_and_tokens',
            'clinics',
            'doctors',
            'patients',
            'appointments',
            'appointment_items',
            'examinations',
        )
