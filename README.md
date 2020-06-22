**Quickstart with Docker:**
1. Checkout docker branch
2. Change configuration to desired values in config/project_config.py
3. Change the following environment variables under "letsencrypt" in the docker-compose.yml file to the desired values:
   - EMAIL
   - URL
   - SUBDOMAINS
4. "docker-compose up"

This automatically creates an admin account with the password defined in config as well as the categories defined in the same file.


**Test Deployment here:** http://helpmap.lucasjeske.de


**Without Docker:**
1. Checkout master branch
2. Change configuration to desired values in '/config/project_config.py'
3. "manage.py initproject"
4. Run locally with "manage.py runserver" or deploy according to your needs
