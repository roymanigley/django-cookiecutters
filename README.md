# Django Cookiecutters
> contains 3 cookiecutters
> - generate project like `django-admin startproject` including `django-rest-framework`
> - generate apps using a rest api like `django-admin startapp` using drf, dj-rest-auth, and api documentation
> - generate apps using django templates like `django-admin startapp` using plain django

## Usage

### create the project

    cookiecutter /absolute/path/to/experiment-cookie-cutter/django_project
    cd cookiecutter_project
    python3 -m venv .venv
    source .venv/bin/activate
    pip install -r requirements.txt
    ./manage.py migrate
    ./manage.py runserver

### customize your models
> adapt them in the `django_app/cookiecutter.json`

### create the api app
> you might adapt the models within `experiment-cookie-cutter/django_api/cookiecutter.json` according fit to your usecase

    cd path/to/project
    cookiecutter /absolute/path/to/experiment-cookie-cutter/django_api

#### adapt `conf/settings.py`
> add the application name to `INSTALLED_APPS`
    
#### adapt `vim conf/urls.py`
> add the path to and include the `application-name.urls`

#### do the migrations

    ./manage.py makemigrations
    ./manage.py migrate

#### add superuser

    ./manage.py createsuperuser

#### run the server

    ./manage.py runserver

### create the template app
> you might adapt the models within `experiment-cookie-cutter/django_template/cookiecutter.json` according fit to your usecase

    cd path/to/project
    cookiecutter /absolute/path/to/experiment-cookie-cutter/django_template

#### adapt `conf/settings.py`
> add the application name to `INSTALLED_APPS`
    
#### adapt `vim conf/urls.py`
> add the path to and include the `application-name.urls`

    urlpatterns += [path('', include('cookiecutter_template_app.urls'))]

#### do the migrations

    ./manage.py makemigrations
    ./manage.py migrate

#### add superuser

    ./manage.py createsuperuser

#### run the server

    ./manage.py runserver

---

## Todo

- [ ] test different model field types
    - [x] `models.CharField`
    - [x] `models.ForeignKey`
    - [ ] `models.Int`
    - [ ] `models.DateField`
    - [ ] `models.DateTimeField`
    - [ ] `models.JsonField`
    - [ ] support for `models.FileField`
- [ ] support for docker
    - database
    - djago
    - nginx
- [ ] use env variables in `conf/settings.py`
    - use dotenv
