# start from an official image
FROM python:3.7

# arbitrary location choice: you can change the directory
RUN mkdir -p /opt/services/djangoapp/src
WORKDIR /opt/services/djangoapp/src

# copy our project code
COPY . /opt/services/djangoapp/src
RUN pip install -r requirements.txt

# expose the port 8000
EXPOSE 3013

RUN python manage.py collectstatic --noinput
COPY ./media /var/www/media

# define the default command to run when starting the container
CMD ./docker-config/scripts/run.sh
