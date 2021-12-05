import os

from django.conf import settings
from django.core.management import BaseCommand, call_command


class Command(BaseCommand):
    def handle(self, *args, **options):

        db_name = settings.DATABASES['default']['NAME']

        if os.path.exists(db_name):
            os.remove(db_name)
            call_command('migrate')
        else:
            print(f'Path {db_name} does not exists')

