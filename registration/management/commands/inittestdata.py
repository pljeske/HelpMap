from django.contrib.auth.models import User
from django.core.management.base import BaseCommand

from config.project_config import CATEGORIES
from map.models import HelpPoint, Category


class Command(BaseCommand):

    def handle(self, *args, **options):
        """
        manage.py inittestdata
        Puts test data in the db.
        """
        print('Creating test data...')
        print('1. Creating test categories...')

        if Category.objects.count() == 0:
            try:
                Category(title="Category1").save()
                Category(title="Category2").save()
                print('Successfully created categories: ' + CATEGORIES)

            except Exception as e:
                print('There was an error while creating the test categories: ' + str(e))
        else:
            print('There are already categories in the database.')

        if HelpPoint.objects.count() == 0:
            try:
                author = User.objects.get(username='admin')
                map_point = {'type': 'Point', 'coordinates': [13.404954, 52.520008]}
                category = Category.objects.get(title='Category1')
                HelpPoint(author=author, title="Test Point1", description="Test Description1",
                          geom=map_point, category=category).save()

                map_point2 = {'type': 'Point', 'coordinates': [13.309320, 52.511860]}
                category2 = Category.objects.get(title='Category2')
                HelpPoint(author=author, title="Test Point2", description="Test Description2",
                          geom=map_point2, category=category2).save()
                print('Successfully created test help points.')
            except Exception as e:
                print('There was an error while creating the test help points: ' + str(e))
        else:
            print('There are already help points in the database.')
