from django.contrib.auth.models import User
from django.core.management.base import BaseCommand
from map.models import Category
from config.project_config import CATEGORIES, INITIAL_ADMIN_PASSWORD


class Command(BaseCommand):

    def handle(self, *args, **options):
        """
        manage.py initproject
        Creates admin account and categories defined in 'config/project_config.py'
        """
        print("Creating admin account...")
        if User.objects.count() == 0:
            username = 'admin'
            email = 'test@test.com'
            print('Creating account for %s (%s)' % (username, email))
            admin = User.objects.create_superuser(email=email, username=username, password=INITIAL_ADMIN_PASSWORD)
            admin.is_active = True
            admin.is_admin = True
            admin.save()
        else:
            print('Admin accounts can only be initialized if no accounts exist!')

        print('Creating categories defined in config/project_config.py...')
        if Category.objects.count() == 0:
            try:
                for category in CATEGORIES:
                    Category(title=category).save()
                print('Successfully created categories: ' + str(CATEGORIES))

            except Exception as e:
                print('There was an error while creating the test categories: ' + str(e))
        else:
            print('There are already categories in the database.')
