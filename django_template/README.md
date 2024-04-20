# Django Template
> generates apps using django templates like `django-admin startapp` using plain django

## Usage

## create the template app
> you might adapt the models within `django_template/cookiecutter.json` according fit to your usecase

    cd path/to/project
    cookiecutter /absolute/path/to/cookiecutter/django_template

### adapt `conf/settings.py`
> add the application name to `INSTALLED_APPS`
    
### adapt `vim conf/urls.py`
> add the path to and include the `application-name.urls`

    urlpatterns += [path('', include('cookiecutter_template_app.urls'))]

### do the migrations

    ./manage.py makemigrations
    ./manage.py migrate

### add superuser

    ./manage.py createsuperuser

### run the server

    ./manage.py runserver
