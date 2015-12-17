from django.core.management.base import BaseCommand, CommandError
from crop.import_data import init_data

class Command(BaseCommand):
    help = 'Init Data'

    def handle(self, *args, **options):
        init_data()
