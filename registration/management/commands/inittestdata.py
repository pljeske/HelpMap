from django.contrib.auth.models import User
from django.core.management.base import BaseCommand
from djgeojson.fields import PointField

from map.models import HelpPoint, Category


class Command(BaseCommand):

    def handle(self, *args, **options):
        print('Creating test data...')
        print('1. Creating test categories...')

        if Category.objects.count() == 0:
            try:
                Category(title="Category1").save()
                Category(title="Category2").save()
                print('Successfully created test categories.')
            except Exception as e:
                print('There was an error while creating the test categories: ' + str(e))
        else:
            print('There are already categories in the database.')

        if HelpPoint.objects.count() == 0:
            try:
                author = User.objects.get(username='admin')
                title = "Test Point"
                description = "Test Description"
                PointField()
                map_point = {'type': 'Point', 'coordinates': [13.404954, 52.520008]}
                category = Category.objects.get(title='Category1')
                HelpPoint(author=author, title=title, description=description, geom=map_point, category=category).save()
                print('Successfully created test help points.')
            except Exception as e:
                print('There was an error while creating the test help points: ' + str(e))
        else:
            print('There are already help points in the database.')

        print('Successfully created test data.')
