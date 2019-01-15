import logging
from django.core.management import BaseCommand
from django.core.management.base import CommandError
from egitim.models import Okul
logger = logging.getLogger('main')

class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument('id', help='fak yu', type=int)

    def handle(self, *args, **options):
        id = options.get('id')
        for_delete = Okul.objects.filter(id=id).delete()
        CommandError("OK!")
