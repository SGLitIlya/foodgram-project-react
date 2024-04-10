import json

from django.conf import settings
from django.core.management.base import BaseCommand

from recipes.models import Ingredient


class Command(BaseCommand):
    """Команда для загрузки данных из json-файлов в БД."""

    FILENAMES_OF_MODELS = [
        ('ingredients.json', Ingredient),
    ]

    help = 'Load data from .json to DB'

    def handle(self, *args, **options):
        print(f'Use path: {options["path"]}')

        for filename, model in self.FILENAMES_OF_MODELS:
            print(f'Load file {filename}')
            with open(f'{options["path"]}/{filename}') as f:
                reader = json.load(f)
                for row in reader:
                    model(**row).save()

        return 'OK'

    def add_arguments(self, parser):
        parser.add_argument(
            '-p',
            '--path',
            action='store',
            default=str(settings.BASE_DIR) + '/core/data',
            help='Path to .json files',
        )
