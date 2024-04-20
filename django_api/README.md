# Django API
> generates apps using a rest api like `django-admin startapp` using drf, dj-rest-auth, and api documentation

## Usage

## create the api app
> you might adapt the models within `django_api/cookiecutter.json` according fit to your usecase

    cd path/to/project
    cookiecutter /absolute/path/to/cookiecutter/django_api

### adapt `conf/settings.py`
> add the application name to `INSTALLED_APPS`
    
### adapt `vim conf/urls.py`
> add the path to and include the `application-name.urls`

### do the migrations

    ./manage.py makemigrations
    ./manage.py migrate

### add superuser

    ./manage.py createsuperuser

### run the server

    ./manage.py runserver

