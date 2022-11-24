"""
Django command to wait for the database
"""

from psycopg2 import OperationalError as Psycopg2Error
import time

from django.db.utils import OperationalError
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    """Django class command to wait for the db"""

    def handle(self, *args, **options):
        ''' Entrypoint for the command '''
        self.stdout.write('Waiting for the database...')
        db_up = False
        while db_up is False:
            try:
                self.check(databases=['default'])
                db_up = True
            except (Psycopg2Error, OperationalError) as err:
                self.stdout.write('Database unavailable, waiting 1 second...')
                print(err)
                time.sleep(1)
        self.stdout.write(self.style.SUCCESS('Database available!'))
