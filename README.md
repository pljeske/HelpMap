**Quickstart (not yet configurable):**
1. Checkout docker3 branch
2. Change ALLOWED_HOSTS in HelpMap/settings.py to desired hostname
3. (Add map/config/keys.py and declare OPENCAGE_API_KEY with you opencage api key)
4. "docker-compose up"

This automatically creates an admin account with password "password" as well as test categories and test help points, so make sure to change these values.


**Test Deployment here:** http://helpmap.lucasjeske.de


**Without Docker:**
1. Checkout master branch
2. Fill in the configuration variables in '/config/project_config.py'
3. "manage.py initproject"
4. Run locally with "manage.py runserver" or deploy according to your needs
