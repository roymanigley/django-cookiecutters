# Django Project
> generates project like `django-admin startproject` including `django-rest-framework`

## Usage

## generate a cookie cutter 
        
    cookiecutter /absolute/path/to/cookiecutter/cookiecutter_generator

## create the project

    cookiecutter /absolute/path/to/cookiecutter/django_project
    cd cookiecutter_project
    python3 -m venv .venv
    source .venv/bin/activate
    pip install -r requirements.txt
    ./manage.py migrate
    ./manage.py runserver

