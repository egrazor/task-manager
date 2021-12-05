from django.core.management import BaseCommand

from tasks.seed.create_seed_tasks import create_base_users, create_seed_tasks, create_user_groups


class Command(BaseCommand):
    def handle(self, *args, **options):
        create_user_groups()
        create_base_users()
        create_seed_tasks()
