from django.core.management.base import BaseCommand
from django.core.management.utils import get_random_secret_key

class Command(BaseCommand):
    help = 'Generates a new Django secret key'

    def handle(self, *args, **kwargs):
        secret_key = get_random_secret_key()
        self.stdout.write(self.style.SUCCESS(f'Generated Secret Key:\n{secret_key}'))
        self.stdout.write(self.style.WARNING(f'\nPut the above secret key in your environment variable or .env file.'))
