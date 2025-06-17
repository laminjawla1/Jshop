from django.core.management.base import BaseCommand, CommandError
from django.core.management import call_command

class Command(BaseCommand):
    help = 'Runs makemigrations for apps in a specified order'

    def handle(self, *args, **options):
        apps = [
                'core',
                'users',
                'brands',
                'categories',
                'locations',
                'products',
                'orders',
            ]

        for app in apps:
            self.stdout.write(self.style.NOTICE(f"🔧 Running makemigrations for '{app}'..."))
            try:
                call_command('makemigrations', app)
            except CommandError as e:
                self.stdout.write(self.style.ERROR(f"❌ Failed on {app}: {e}"))
        # call_command('migrate')
