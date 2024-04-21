# Django Cookiecutters
> this repo contains multiple cookiecutters

## [cookiecutter_generator](cookiecutter_generator)
> - generates a cookiecutter
## [django_project](django_project)
> - generate project like `django-admin startproject` including `django-rest-framework`
## [django_api](django_api)
> - generate apps using a rest api like `django-admin startapp` using drf, dj-rest-auth, and api documentation
## [django_template](django_template)
> - generate apps using django templates like `django-admin startapp` using plain django

---

## Todo

- [ ] test different model field types
    - [x] `models.CharField`
    - [x] `models.ForeignKey`
    - [x] `models.EmailField`
    - [x] `models.BooleanField`
    - [ ] `models.BinaryField`
    - [ ] `models.DecimalField`
    - [ ] `models.BigIntegerField`
    - [x] `models.IntegerField`
    - [x] `models.FloatField`
    - [x] `models.DateField`
    - [x] `models.DateTimeField`
    - [ ] `models.DurationField`
    - [x] `models.JsonField`
    - [ ] `models.FileField`
- [ ] support for docker
    - database
    - djago
    - nginx
- [ ] use env variables in `conf/settings.py`
    - use dotenv
