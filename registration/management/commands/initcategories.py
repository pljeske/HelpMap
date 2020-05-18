from django.core.management.base import BaseCommand
from map.models import Category


class Command(BaseCommand):

    def handle(self, *args, **options):
        if Category.objects.count() == 0:
            Category(title="Category1").save()
            Category(title="Category2").save()
        else:
            print('There are already categories in the database.')