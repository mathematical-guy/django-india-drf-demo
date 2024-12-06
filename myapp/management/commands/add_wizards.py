from django.core.management.base import BaseCommand


from myapp.utils import make_request_to_wizard_api


class Command(BaseCommand):
    help = 'Add Wizard'

    def handle(self, *args, **kwargs):
        make_request_to_wizard_api()

