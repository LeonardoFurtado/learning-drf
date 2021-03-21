from django.core.management.base import BaseCommand, CommandError
from core.models import Author
import csv

class Command(BaseCommand):
    help = 'Import authors from a csv file.'

    def add_arguments(self, parser):
        parser.add_argument('--path', type=str, help="file path")

    def handle(self, *args, **options):
        path = options['path']
        with open(path) as f:
            reader = csv.reader(f)
            for row in reader:
                if row[0] == 'name':
                    continue
                _, created = Author.objects.get_or_create(
                    name=row[0],
                    )
